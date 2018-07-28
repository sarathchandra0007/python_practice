def anagram(a,b):
    a=a.replace(' ','').lower()
    b=b.replace(' ','').lower()
    a=sorted(a)
    b=sorted(b)

    if a==b:
        return "anagram"
    return "not"


print (anagram('cata','tac a'))
