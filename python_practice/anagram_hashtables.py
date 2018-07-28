def anagram(s1,s2):
    s1=s1.replace(' ','').lower()
    s2=s2.replace(' ','').lower()

    if len(s1)!=len(s2):
        return False
    
    sample={}

    for i in s1:
        if i in sample:
            sample[i]+=1
        else:
            sample[i]=1

    print (sample)

    for i in s2:
        if i in sample:
            sample[i]-=1
    
    for i in sample:
        if sample[i]!=0:
            return False
    return True

print (anagram('sarath','sar tha'))
