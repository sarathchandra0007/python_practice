def rev_word(s):
    string=" ".join(reversed(s.split()))
    string1=" ".join(s.split()[::-1])
    print (string1)
    return string

print (rev_word("Hi John,   are you ready to go?"))
