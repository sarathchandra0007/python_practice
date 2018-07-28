def uni_char(s):
    a=dict()
    for i in s:
        if i in a:
            return False
        else:
            a[i]=1
    return True

print (uni_char('aabcde'))

s='aassdassss'
print (len(set(s)))
