import sys
def fama(text):
    result=[]
    for c in text:
        if c.islower():
            n=chr(ord('z')-(ord(c)-ord('a')))
        elif c.isupper():
            n=chr(ord('Z')-(ord(c)-ord('A')))
        else:n=c
        result.append(n)
    return ''.join(result)
p=input()
print(fama(p))
