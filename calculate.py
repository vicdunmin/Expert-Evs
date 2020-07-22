import math
import json

with open('data/nature.json', 'r') as fp:
    nature_dict = json.load(fp)


class stat(object):

    def __init__(self, poke_dict, HP_IV=31, Def_IV=31, Spd_IV=31,
                 disposable=510, level=100, phys_weight=0.5, allow_nature=True,
                 phys_mod=1.0, spec_mod=1.0, method='c'):
        self.HP = poke_dict['HP']
        self.Def = poke_dict['Def']
        self.Spd = poke_dict['Spd']
        self.Atk = poke_dict['Atk']
        self.Spa = poke_dict['Spa']
        self.HP_IV = HP_IV
        self.Def_IV = Def_IV
        self.Spd_IV = Spd_IV
        self.disposable = disposable
        self.level = level
        self.nature_dict = nature_dict
        self.phys_weight = phys_weight
        self.spa_weight = 1.0 - phys_weight
        self.phys_mod = phys_mod
        self.spec_mod = spec_mod
        self.allow_nature = allow_nature

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

    def valid_evs(self, hp_ev, def_ev, spd_ev):
        if hp_ev > 252 or def_ev > 252 or spd_ev > 252:
            return False
        if sum([hp_ev, def_ev, spd_ev]) > self.disposable:
            return False
        return True

    def calc(self):
        max_score = 0
        for hp_ev in range(0, self.disposable + 1, 4):
            for def_ev in range(0, self.disposable + 1, 4):
                for spd_ev in range(0, self.disposable + 1, 4):
                    if self.valid_evs(hp_ev, def_ev, spd_ev):
                        for nat in self.nature_dict:
                            if "Def" in self.nature_dict[nat]:
                                def_mod = float(
                                    self.nature_dict[nat]["Def"])
                                spd_mod = 1.0
                            elif "Spd" in self.nature_dict[nat]:
                                spd_mod = float(
                                    self.nature_dict[nat]["Spd"])
                                def_mod = 1.0
                            if not self.allow_nature:
                                def_mod = spd_mod = 1.0
                            hp_stat = self.hp_transform(hp_ev)
                            def_stat = self.def_transform(
                                def_ev, def_mod) * self.phys_mod
                            spd_stat = self.spd_transform(
                                spd_ev, spd_mod) * self.spec_mod
                            score = hp_stat / \
                                (self.phys_weight / def_stat +
                                 self.spa_weight / spd_stat)
                            if (score > max_score):
                                max_score = score
                                if not self.allow_nature:
                                    max_comb = [hp_ev, def_ev,
                                                spd_ev, 'no nature', None]
                                else:
                                    if nat == 'Bold' or nat == 'Impish':
                                        nat = '+Def'
                                        if int(self.Atk) >= int(self.Spa):
                                            rec_nat = 'Impish'
                                        else:
                                            rec_nat = 'Bold'
                                    else:
                                        nat = '+Spd'
                                        if (int(self.Atk) >= int(self.Spa)):
                                            rec_nat = 'Careful'
                                        else:
                                            rec_nat = 'Calm'
                                    max_comb = [hp_ev, def_ev,
                                                spd_ev, nat, rec_nat]
        return max_comb
