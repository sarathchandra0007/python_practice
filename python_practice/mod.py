def sum_(n):
    if n<10:
        return n
    else:
        res=0
        cop=n%10
        res=res+cop
        return res+sum_(n//10)
    
print (sum_(12345))
