from get_stat import get_info
from calculate import stat
import json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pokemon',
                        help='Select the pokemon you want to EV')
    parser.add_argument('-d', '--disposable',
                        help='The EVs to be put into bulk calculation', default=510)
    parser.add_argument(
        '-n', '--nature', help='whether or not to allow nature modifier', default=True)
    parser.add_argument('-pw', '--phys_weight',
                        help='physical weight of the bulk of the pokemon', default=0.5)
    parser.add_argument('-pm', '--phys_modifier',
                        help='physical phys_modifier of the bulk of the pokemon', default=1.0)
    parser.add_argument('-sm', '--spec_modifier',
                        help='special phys_modifier of the bulk of the pokemon', default=1.0)
    parser.add_argument(
        '-m', '--method', help='either the chinese method or smogon method', default='c')
    args = parser.parse_args()

    poke_name = args.pokemon.lower()
    disposable_ev = int(args.disposable)
    if args.nature == 'false' or args.nature == 'False':
        nature = False
    else:
        nature = True
    phys_weight = float(args.phys_weight)
    phys_modifier = float(args.phys_modifier)
    spec_modifier = float(args.spec_modifier)
    method = args.method

    with open('data/poke_stat.json', 'r') as fp:
        poke_stat = json.load(fp)
    if poke_name not in poke_stat:
        poke_stat = get_info(poke_name, poke_stat)
        with open('data/poke_stat.json', 'w') as fp:
            json.dump(poke_stat, fp)
    p_stat = stat(poke_stat[poke_name],
                  disposable=disposable_ev, phys_weight=phys_weight,
                  phys_mod=phys_modifier, spec_mod=spec_modifier,
                  allow_nature=nature,
                  method=method)
    hp_ev, def_ev, spd_ev, nat, rec_nat = p_stat.calc()
    print('Pokemon name: {}, Disposable Total EVs: {}'.format(
        poke_name, disposable_ev))
    print('EVs: {} HP / {} Def / {} Spd'.format(hp_ev, def_ev, spd_ev))
    print('Nature modifier: {}, Recommended nature: {}'.format(nat, rec_nat))
