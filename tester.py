"""
import base64

def shorten_url(long_url):
    char_list = []
    for char in long_url:
        if char not in char_list:
            char_list.append(char)

    shortend_url = ''.join(char_list)
    print(shortend_url)

    ascii_string = shortend_url.encode('ascii')
    encoded = base64.b64encode(ascii_string)
    short_url = encoded.decode('ascii')
    return short_url

someVar = shorten_url('www.test.com/index.html')
"""
from math import floor
import string

def toBase62(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

print(toBase62(10000))
print(toBase62(1))
print(toBase62(61))
print(toBase62(62))

#print(len(someVar))
#print(someVar)
