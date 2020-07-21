from get_stat import get_info
from calculate import stat
import json


if __name__ == '__main__':
    poke_name = input(
        'Please enter in the pokemon name you want to calculate: ').lower()
    with open('data/poke_stat.json', 'r') as fp:
        poke_stat = json.load(fp)
    if poke_name not in poke_stat:
        poke_stat = get_info(poke_name, poke_stat)
        with open('data/poke_stat.json', 'w') as fp:
            json.dump(poke_stat, fp)
    p_stat = stat(poke_stat[poke_name])
    print(p_stat.calc())
