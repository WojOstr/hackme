# Synapsi Hackme Subpage - Attempt to solve [Not Done]

## My attempt to solve Synapsi.xyz hackme subpage with Python, BeautifulSoup and pyenchant.

[link to hackme](https://synapsi.xyz/hackme)

When we access page you see bordered encoded message, which is changing every time you refresh the page. 
I thought of kinda automating the proccess of scraping the message into code by using BeatifulSoup and urllib, 
and then processing it with Python. Cipher used to encode message is hidden on site - but Encoding includes two 
random values - b and c - which values are unknown to user which makes it harder to decode message.
I've tried making thousands of alphabets based on range values (ex. b = 1, c = 1; b = 2, c = 1) to use it to decode encoded message, with no success so far.

## Encode and decode example

Consider following code:

```
import string
encode = lambda a,b,c:(d:=0)or[pow(string.printable.index(e)*c+b+d,101,97) for e in a]
encoded_text = encode('Congratulations, this is a test encoding done for github Readme.md! Welcome all readersC', 10, 3)
```

You receive list of ints, which contains encoded text. 

```
[85, 38, 89, 60, 81, 10, 0, 49, 9, 10, 0, 33, 38, 89, 48, 61, 1, 0, 35, 33, 48, 1, 33, 48, 1, 10, 1, 0, 19, 48, 0, 1, 19, 89, 63, 38, 94, 33, 89, 60, 1, 94, 38, 89, 19, 1, 69, 38, 81, 1, 60, 33, 0, 35, 49, 93, 1, 44, 19, 10, 94, 84, 19, 80, 84, 94, 32, 1, 7, 19, 9, 63, 38, 84, 19, 1, 10, 9, 9, 1, 81, 19, 10, 94, 19, 81, 48, 85]
```

Let's break it down to every step of lambda function:

```
C = string.printable.index('C')     #assing index of string.printable 'C' to variable C
print(C)                            #prints 38
C = C * 3 + 10 + 0                  #next step of lambda function, multiply by c and both b and d.
print(C)                            #prints 124
print(pow(C, 101))                  #power 124 to 101 (Prints huge number)
print(pow(C, 101, 97))              #power 124 to 101 and divide the result and find the remainder (C ^ 101 % 97), prints 85
```

So, we know b and c values in this example - let's try to decode it by creating dictonary of encoded letters using known formula

```
def list_to_int(inp: list)-> int:
    """Turn list to int"""
    return int(''.join([str(x) for x in inp]))
d = {}
for x in string.printable:
    d[list_to_int(encode(x, 10, 3))] = x
```

Once we have dictonary, we can just simply match the keys of dictonary with every letter from encoded text and get its values. Simpy as that

```
final_string = ''
for letter in encoded_text:
    final_string += d.get(letter, '')
```

## Conclusion


 -So once we know how these values are being calculated, all we need to know is how to get the actual b and c used in actual encoded text from hackme subpage. 
 -I don't know what the result should be - if it contains english words, then i might use pyenchant to search only for english words (and skip iterations that don't have them)
