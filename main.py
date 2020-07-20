import sys
import codecs
from urllib import request
from bs4 import BeautifulSoup

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

url = "https://wiki.52poke.com/wiki/celebi"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode(
    'utf-8')

soup = BeautifulSoup(page_info, 'html.parser')

titles = soup.find('tr', 'bgl-HP').stripped_strings

for t in titles:
    print(t)
