# Synapsi Hackme Subpage - Attempt to solve [Not Done]

## My attempt to solve Synapsi.xyz hackme subpage with Python, BeautifulSoup and pyenchant.

[link to hackme](https://synapsi.xyz/hackme)

When we access page you see bordered encoded message, which is changing every time you refresh the page. 
I thought of kinda automating the proccess of scraping the message into code by using BeatifulSoup and urllib, 
and then processing it with Python. Cipher used to encode message is hidden on site - but Encoding includes two 
random values - b and c - which values are unknown to user which makes it harder to decode message.
I've tried making thousands of alphabets based on range values (ex. b = 1, c = 1; b = 2, c = 1) to use it to decode encoded message, with no success so far.

I don't know what the result should be - if it contains english words, then i might use pyenchant to search only for english words (and skip iterations that don't have them)
