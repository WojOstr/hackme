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

```python
import string
encode = lambda a,b,c:(d:=0)or[pow(string.printable.index(e)*c+b+d,101,97) for e in a]
encoded_text = encode('Congratulations, this is a test encoding done for github Readme.md! Welcome all readersC', 10, 3)
```

You receive list of ints, which contains encoded text. 

```python
[85, 38, 89, 60, 81, 10, 0, 49, 9, 10, 0, 33, 38, 89, 48, 61, 1, 0, 35, 33, 48, 1, 33, 48, 1, 10, 1, 0, 19, 48, 0, 1, 19, 89, 63, 38, 94, 33, 89, 60, 1, 94, 38, 89, 19, 1, 69, 38, 81, 1, 60, 33, 0, 35, 49, 93, 1, 44, 19, 10, 94, 84, 19, 80, 84, 94, 32, 1, 7, 19, 9, 63, 38, 84, 19, 1, 10, 9, 9, 1, 81, 19, 10, 94, 19, 81, 48, 85]
```

Let's break it down to every step of lambda function:

```python
C = string.printable.index('C')     #assing index of string.printable 'C' to variable C
print(C)                            #prints 38
C = C * 3 + 10 + 0                  #next step of lambda function, multiply by c and both b and d.
print(C)                            #prints 124
print(pow(C, 101))                  #power 124 to 101 (Prints huge number)
print(pow(C, 101, 97))              #power 124 to 101 and divide the result and find the remainder (C ^ 101 % 97), prints 85
```

So, we know b and c values in this example - let's try to decode it by creating dictonary of encoded letters using known formula

```python
def list_to_int(inp: list)-> int:
    """Turn list to int"""
    return int(''.join([str(x) for x in inp]))
d = {}
for x in string.printable:
    d[list_to_int(encode(x, 10, 3))] = x
```

Once we have dictonary, we can just simply match the keys of dictonary with every letter from encoded text and get its values. Simpy as that

```python
final_string = ''
for letter in encoded_text:
    final_string += d.get(letter, '')
```
### Result

<details><summary>Step by step results of decoding</summary>

```console
85 
38 C
89 Co
60 Con
81 Cong
10 Congr
0 Congra
49 Congrat
9 Congratu
10 Congratul
0 Congratula
33 Congratulat
38 Congratulati
89 Congratulatio
48 Congratulation
61 Congratulations
1 Congratulations,
0 Congratulations, 
35 Congratulations, t
33 Congratulations, th
48 Congratulations, thi
1 Congratulations, this
33 Congratulations, this 
48 Congratulations, this i
1 Congratulations, this is
10 Congratulations, this is 
1 Congratulations, this is a
0 Congratulations, this is a 
19 Congratulations, this is a t
48 Congratulations, this is a te
0 Congratulations, this is a tes
1 Congratulations, this is a test
19 Congratulations, this is a test 
89 Congratulations, this is a test e
63 Congratulations, this is a test en
38 Congratulations, this is a test enc
94 Congratulations, this is a test enco
33 Congratulations, this is a test encod
89 Congratulations, this is a test encodi
60 Congratulations, this is a test encodin
1 Congratulations, this is a test encoding
94 Congratulations, this is a test encoding 
38 Congratulations, this is a test encoding d
89 Congratulations, this is a test encoding do
19 Congratulations, this is a test encoding don
1 Congratulations, this is a test encoding done
69 Congratulations, this is a test encoding done 
38 Congratulations, this is a test encoding done f
81 Congratulations, this is a test encoding done fo
1 Congratulations, this is a test encoding done for
60 Congratulations, this is a test encoding done for 
33 Congratulations, this is a test encoding done for g
0 Congratulations, this is a test encoding done for gi
35 Congratulations, this is a test encoding done for git
49 Congratulations, this is a test encoding done for gith
93 Congratulations, this is a test encoding done for githu
1 Congratulations, this is a test encoding done for github
44 Congratulations, this is a test encoding done for github 
19 Congratulations, this is a test encoding done for github R
10 Congratulations, this is a test encoding done for github Re
94 Congratulations, this is a test encoding done for github Rea
84 Congratulations, this is a test encoding done for github Read
19 Congratulations, this is a test encoding done for github Readm
80 Congratulations, this is a test encoding done for github Readme
84 Congratulations, this is a test encoding done for github Readme.
94 Congratulations, this is a test encoding done for github Readme.m
32 Congratulations, this is a test encoding done for github Readme.md
1 Congratulations, this is a test encoding done for github Readme.md!
7 Congratulations, this is a test encoding done for github Readme.md! 
19 Congratulations, this is a test encoding done for github Readme.md! W
9 Congratulations, this is a test encoding done for github Readme.md! We
63 Congratulations, this is a test encoding done for github Readme.md! Wel
38 Congratulations, this is a test encoding done for github Readme.md! Welc
84 Congratulations, this is a test encoding done for github Readme.md! Welco
19 Congratulations, this is a test encoding done for github Readme.md! Welcom
1 Congratulations, this is a test encoding done for github Readme.md! Welcome
10 Congratulations, this is a test encoding done for github Readme.md! Welcome 
9 Congratulations, this is a test encoding done for github Readme.md! Welcome a
9 Congratulations, this is a test encoding done for github Readme.md! Welcome al
1 Congratulations, this is a test encoding done for github Readme.md! Welcome all
81 Congratulations, this is a test encoding done for github Readme.md! Welcome all 
19 Congratulations, this is a test encoding done for github Readme.md! Welcome all r
10 Congratulations, this is a test encoding done for github Readme.md! Welcome all re
94 Congratulations, this is a test encoding done for github Readme.md! Welcome all rea
19 Congratulations, this is a test encoding done for github Readme.md! Welcome all read
81 Congratulations, this is a test encoding done for github Readme.md! Welcome all reade
48 Congratulations, this is a test encoding done for github Readme.md! Welcome all reader
85 Congratulations, this is a test encoding done for github Readme.md! Welcome allreaders
Congratulations, this is a test encoding done for github Readme.md! Welcome all readersC
```
</details>

## Conclusion


 - So once we know how these values are being calculated, all we need to know is how to get the actual b and c used in actual encoded text from hackme subpage. 
 - I don't know what the result should be - if it contains english words, then i might use pyenchant to search only for english words (and skip iterations that don't have them)
