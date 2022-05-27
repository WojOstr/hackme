import string
from collections import Counter
from bs4 import BeautifulSoup
import urllib.request
import re
import json

def list_to_int(inp: list)-> int:
    return int(''.join([str(x) for x in inp]))

def encoded_to_list_int(inp: str)-> list:
    return [string.printable.index(str(x)) for x in inp]

def request_cipher()->str:
    url = "https://synapsi.xyz/hackme"
    url_contents = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(url_contents, features='html.parser')
    div = soup.find("div", {"class": "cipher"})
    return str(div.find('p').text)

def delete_copies(l: list)->list:
    seen = set()
    new_l = []
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return new_l

test = request_cipher()
print(test)

#for i, x in enumerate(string.printable):
    #print(x, i)

encode=lambda a,b,c:(d:=0)or[pow(string.printable.index(e)*c+b+d,101,97) for e in a]
"""
l = []
for i in range(1000):
    for j in range(1000):
        separate_d = {}
        for x in string.printable:
            separate_d[list_to_int(encode(x, i,  j))] = x

        if separate_d != {}:
            l.append(separate_d)
new_l = delete_copies(l)


with open('data.json', 'w+', encoding='utf-8') as f:
    json.dump(new_l, f, ensure_ascii=False, indent=4)
"""


with open('data.json', 'r') as f:
  data = json.load(f)


for x in data:
    s = ''
    break_out_flag = False
    for letter in encoded_to_list_int(test):
        if letter > 76:
            break_out_flag = True
            break
        s += x.get(letter, ' ')

    if not break_out_flag:
        with open(r'Failed.txt', 'a+') as file:
            file.write(s)
            file.write('\n\n\n ---------------------------------------------------------------- \n\n\n')


