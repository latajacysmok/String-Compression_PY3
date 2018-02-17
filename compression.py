import re
import random
import string

def compress(s):
    news=""
    while True:
        if len(s)==0:
            print(news)
            return news
        f= s[0]
        l=len(s)
        s = re.sub(r"^"+f+"*","",s)
        news += str(l- len(s)) + f

# compress("AAABBBBCAAAaaDD")

def decompress(w):
    news = ""
    num = 0
    for sign in w:
        try:
            int(sign)
            num = int(sign)

        except:
            news += num*sign

    print(news)
    return news

# decompress("3A4B1C3A2a2D")

def test(n):
    for i in range(n):
        x = random.randint(1, 30)
        y = random.sample(string.ascii_letters, x)
        a = "".join(y)
        print(a == decompress(compress(a)))

# test(3)