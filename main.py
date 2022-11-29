import string
from bs4 import BeautifulSoup
import urllib.request
import json
from collections import Counter
import enchant

def list_to_int(inp: list)-> int:
    """Turn list to int"""
    return int(''.join([str(x) for x in inp]))

def encoded_to_list_int(inp: str)-> list:
    """Return list of indexes in string.printable from str input"""
    return [string.printable.index(str(x)) for x in inp]

def check_frequency_of_letters(inp: str)-> list:
    """Checks frequency of letters in str"""
    c = Counter(inp)
    return c.most_common(1)

def request_cipher()->str:
    """Scrap website for specific div consiting of encoded message and returns it"""
    url = "https://synapsi.xyz/hackme"
    url_contents = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(url_contents, features='html.parser')
    div = soup.find("div", {"class": "cipher"})
    return str(div.find('p').text)

def delete_copies(l: list)->list:
    """Delete same duplicates from list and return new list"""
    seen = set()
    new_l = []
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return new_l

def create_alphabet(b, c):
    """Creates encoded alphabet with b and c range, dumps result into json file"""
    l = []
    for i in range(b + 1):
        for j in range(c + 1):
            separate_d = {}
            for x in string.printable:
                separate_d[list_to_int(encode(x, i,  j))] = x
            if separate_d != {}:
                l.append(separate_d)
    new_l = delete_copies(l)
    with open('data.json', 'w+', encoding='utf-8') as f:
        json.dump(new_l, f, ensure_ascii=False, indent=4)


#'VggyOSAGBz4BFiE+UV9NMF9SEBMxUTpJHxMWOS9TPilWDElYGy0wM0IzQg9CCA43IjcQD19ZBDUVFRUcDCs4QF9OCBEKPCoUUABbEQpWGwUJGUlWWhwbEQIMEA9CXRUBAhobSyNRBEtdRDs2FUQaXAYcVEUaMjtBQik1CFZaDkFaRQ0GB0tgTDJGUUAEEwo6HFcnWjhPN1RaUBUZB1ocKRJCCB0CTQNgK1lMGQ5WTU4gS0MQACU8G0tDGwMCJ1IsLg8+SBFZKh4iIggMQAcxAV4IVx4UUAgfTApKYCMeWUkwXzpZUAw7QUI3QwAtB0VHRQpWJjowDE9YJTxYOAoCBRRQX1lKL1o8WgpIXUoCQSYeIlglUkBGCypHTDtdIiY6FhdRFSYqISZcBkVIKwoQIkUNMRNFRys/UixMICgHBElXKBIlWUwKPDM9VyUJLQcxOFVaHR4CBUItSTAAB0VHDDsfVRFDEiUuMDlPMUMiKSQAMVEoGDpZUCEEKD46BChdTkE7EBRLLAkbQTZLAFskRgs4VUkMK0wsHQIVKWBDNyhLYFxBRCEYVREnJkYGDhgsOx8qSgxANBhOREAJGS5YUU0uWzskGks6WRQWXUcwXwkbQQdFTzFOXl9NIxAhBAAkRgQsLjYnNkdMATYQQBAPORYMHUpKQR8qAi8pSTA/Oh1NARhDTg49SiFbMDkUNk5eCC0OJlwZLkEtMCIIVAUZPyxJNVxdADFGFl08VlglUhAbAyFbDiQ6BD8XOks4Ty0xRAg8GwMTOxgsHS9gQkQSNidbBy0LMAInGCwgSFNMUjIgSCMvWjg4OjFRFxowM1MqJyQsAiIIDj4/DVo9G1Q9JhZHFl0eSFswAA0wGwMTSVgbIi0HMUgSAhgALjRTKidaDj0pDykkTg49TQkZCS0+AiJYGx8gHS8RSk0uND4oI1c5STUPKRg5AkYHSzkECkocXzsSJUJEIRg='

encode=lambda a,b,c:(d:=0)or[pow(string.printable.index(e)*c+b+d,101,97) for e in a] # Cipher, a = string, b and c are unknown values


def decode_cipher_by_alphabet(inp = ''):
    """Function takes encoded message as input and try to decode it by 
    iterate over json with encoded alphabets in dict and compare values. 
    When whole inp is 'decoded', result is being saved to txt file."""
    d = enchant.Dict("en_US")
    with open('data.json', 'r') as f:
        data = json.load(f)
    if inp != '':
        cipher = inp
    else:
        cipher = request_cipher()
    for alphabet_coded in data:
        final_string = ''
        for letter in encoded_to_list_int(cipher[:30]):
            final_string += alphabet_coded.get(str(letter), ' ')

        if d.check(final_string.split()[0]): 
            with open('result_data.txt', 'a+') as file:
                file.write(final_string)
                file.write('\n\n\n ----------------------------------------------------------- \n\n\n')

#word = 'VggyOSAGBz4BFiE+UV9NMF9SEBMxUTpJHxMWOS9TPilWDElYGy0wM0IzQg9CCA43IjcQD19ZBDUVFRUcDCs4QF9OCBEKPCoUUABbEQpWGwUJGUlWWhwbEQIMEA9CXRUBAhobSyNRBEtdRDs2FUQaXAYcVEUaMjtBQik1CFZaDkFaRQ0GB0tgTDJGUUAEEwo6HFcnWjhPN1RaUBUZB1ocKRJCCB0CTQNgK1lMGQ5WTU4gS0MQACU8G0tDGwMCJ1IsLg8+SBFZKh4iIggMQAcxAV4IVx4UUAgfTApKYCMeWUkwXzpZUAw7QUI3QwAtB0VHRQpWJjowDE9YJTxYOAoCBRRQX1lKL1o8WgpIXUoCQSYeIlglUkBGCypHTDtdIiY6FhdRFSYqISZcBkVIKwoQIkUNMRNFRys/UixMICgHBElXKBIlWUwKPDM9VyUJLQcxOFVaHR4CBUItSTAAB0VHDDsfVRFDEiUuMDlPMUMiKSQAMVEoGDpZUCEEKD46BChdTkE7EBRLLAkbQTZLAFskRgs4VUkMK0wsHQIVKWBDNyhLYFxBRCEYVREnJkYGDhgsOx8qSgxANBhOREAJGS5YUU0uWzskGks6WRQWXUcwXwkbQQdFTzFOXl9NIxAhBAAkRgQsLjYnNkdMATYQQBAPORYMHUpKQR8qAi8pSTA/Oh1NARhDTg49SiFbMDkUNk5eCC0OJlwZLkEtMCIIVAUZPyxJNVxdADFGFl08VlglUhAbAyFbDiQ6BD8XOks4Ty0xRAg8GwMTOxgsHS9gQkQSNidbBy0LMAInGCwgSFNMUjIgSCMvWjg4OjFRFxowM1MqJyQsAiIIDj4/DVo9G1Q9JhZHFl0eSFswAA0wGwMTSVgbIi0HMUgSAhgALjRTKidaDj0pDykkTg49TQkZCS0+AiJYGx8gHS8RSk0uND4oI1c5STUPKRg5AkYHSzkECkocXzsSJUJEIRg='
#word2 = 'BERMFjoMWDYCTggMNU0FNzQ4IF1PTTcNEyQBPgZeNgAnIgxLDUtKQ0knFE8dIVQWQllFO0NZIh4COFMOIj8iA0szKk8LXCsEMh9dRRFSMwgrJi8fXC1XMTsyCRNDWyYCFVVQP01KEERdJQhOGRIOHglDQBM8EEtCG0YmABcLFipZIjMGCCtCQBM8ECIsWj4AGwoJMFFNEiMWRkZXXjorGhIQIhoPCTA7QVReM0ZWOV9QEkUdUBozQl89ARkXKkYfXRA6U0FVNUwWHVAcORkSSCcmCTIGXj5VSwIhAyQJGSkXPSIeAgosRTtBVQwwRj5PUTMwOxVfSlBDQFodBggzMEdEEC4SUjFYJl8aOEQUF1sIIixaHitCQCIAXRonMTsVH0c6NhkSQCBdJSwRUg0eMzApWQQ7FT5VWA4eRFFLMxAdCz9JVxMtQC0QOmAfUzUhVBZSAz8vShItXw88LzpOWCgUKRcXPSxZPQhNTF0dLF9aBAtgN0c+XB0KSCYxFyMUViJTDTlPMzdERTc+LjxgPi4SHlA/FSFTQR9BSCkiABcLPzZDSko7OU4ZUytPRElNRT4xIysNRiEHTBZXLhsMIgE6NhIRWw5XYD4uHStWLhs4IBgfQRAdR0Q2Qxo3AR9BVC0+WEsKCQM/ASUxTBwGUE4CAk4mUVUFUwVTFlIwPi4SDixFGhJZPTlYIEtCGkZPNUwYKi0YOFMMRTggK080OFEyK080QTE+VVQ/ASFPCQZRVS1KCABYKh5TXgoAJAUGUChFWhU+XF8kOQUDUEwnL0pDHjA6NgsyBlEyEiMARgZGJihZNhwTJBlKGCMgQ0kDP10qTzVTQVQWAjg/SRgkAwhDGkdJJR0lNgJOTjM3RBA6MRw5U1hIGyFBSEIeCU4ZGwwDOw0BCkglNUwWXyQyK1o+NlBOC1gqHlMvJlsQNlEcOUxEKkY+IDApGjNEERAuGhJXWzlBVl86DAUKSB9dX1dVExA6NAYzJzYzCCtCWxETHglgHwgiEi1XVT45FiMUVkgbRyZbES4SOUwiHhslYCM/By9IDygiPzUKLCdAKTBJIyBTMEpeVjI9GiMBAjc='
#decode_cipher_by_alphabet(word2)

decode_cipher_by_alphabet()