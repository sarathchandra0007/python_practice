import itertools

def permutation(s):
    return list(itertools.permutations(s))

def permu(s):
    out=[]

    if len(s)==1:
        output=[s]
    else:
        for index,i in enumerate(s):
            


permu('abc')
print (permutation('abc'))
