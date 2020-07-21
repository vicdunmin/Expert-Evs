import math
import json

with open('data/nature.json', 'r') as fp:
    nature = json.load(fp)


class stat(object):

    def __init__(self, poke_dict, HP_IV=31, Def_IV=31, Spd_IV=31, disposable=510, level=100, phys_weight=0.4, no_nature=False):
        self.HP = poke_dict['HP']
        self.Def = poke_dict['Def']
        self.Spd = poke_dict['Spd']
        self.HP_IV = HP_IV
        self.Def_IV = Def_IV
        self.Spd_IV = Spd_IV
        self.disposable = disposable
        self.level = level
        self.nature_dict = nature
        self.phys_weight = phys_weight
        self.spa_weight = 1.0 - phys_weight
        self.no_nature = no_nature

    def hp_transform(self, ev):
        hp_stat = ((2 * self.HP + self.HP_IV + ev // 4)
                   * self.level) // 100 + self.level + 10
        return hp_stat

    def def_transform(self, ev, nature_mod=1.0):
        other_stat = (((2 * self.Def + self.Def_IV + ev // 4)
                       * self.level) // 100 + 5) * nature_mod
        return math.floor(other_stat)

    def spd_transform(self, ev, nature_mod=1.0):
        other_stat = (((2 * self.Spd + self.Spd_IV + ev // 4)
                       * self.level) // 100 + 5) * nature_mod
        return math.floor(other_stat)

    def calc(self):
        max_score = 0
        for hp_ev in range(0, 255, 4):
            for def_ev in range(0, 255, 4):
                sum_ev = hp_ev + def_ev
                if sum_ev < 255:
                    continue
                else:
                    for spd_ev in range(0, self.disposable - sum_ev + 1, 4):
                        for nat in self.nature_dict:
                            if "Def" in self.nature_dict[nat]:
                                def_mod = float(self.nature_dict[nat]["Def"])
                                spd_mod = 1.0
                            elif "Spd" in self.nature_dict[nat]:
                                spd_mod = float(self.nature_dict[nat]["Spd"])
                                def_mod = 1.0
                            else:
                                def_mod = spd_mod = 1.0
                            hp_stat = self.hp_transform(hp_ev)
                            def_stat = self.def_transform(def_ev, def_mod)
                            spd_stat = self.spd_transform(spd_ev, spd_mod)
                            score = hp_stat / \
                                (self.phys_weight / def_stat +
                                 self.spa_weight / spd_stat)
                            if (score > max_score):
                                max_score = score
                                max_comb = [hp_ev, def_ev, spd_ev, nat]
        return max_comb
