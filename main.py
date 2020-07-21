from get_stat import get_info
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
    print(poke_stat[poke_name])
