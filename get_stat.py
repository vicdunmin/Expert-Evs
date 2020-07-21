import sys
import codecs
from urllib import request
from bs4 import BeautifulSoup

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def get_stat(code):
    l = list()
    for c in code:
        l.append(c)
    return l[2]


def get_info(poke_name, poke_stat):

    url = "https://wiki.52poke.com/wiki/{}".format(poke_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url, headers=headers)
    try:
        page_info = request.urlopen(page).read().decode(
            'utf-8')
    except:
        print('Pokemon Not Found')
        exit(-1)

    soup = BeautifulSoup(page_info, 'html.parser')
    hp_code = soup.find('tr', 'bgl-HP').stripped_strings
    phys_att_code = soup.find('tr', 'bgl-攻击').stripped_strings
    phys_def_code = soup.find('tr', 'bgl-防御').stripped_strings
    spe_att_code = soup.find('tr', 'bgl-特攻').stripped_strings
    spe_def_code = soup.find('tr', 'bgl-特防').stripped_strings
    speed_code = soup.find('tr', 'bgl-速度').stripped_strings

    poke_stat[poke_name] = key = dict()
    key['HP'] = int(get_stat(hp_code))
    key['Atk'] = int(get_stat(phys_att_code))
    key['Def'] = int(get_stat(phys_def_code))
    key['Spa'] = int(get_stat(spe_att_code))
    key['Spd'] = int(get_stat(spe_def_code))
    key['Spe'] = int(get_stat(speed_code))

    return poke_stat
