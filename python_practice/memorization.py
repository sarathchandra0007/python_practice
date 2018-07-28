fib_mem={}

def fibonocii(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    if not n in fib_mem:
        print ("hi")
        fib_mem[n]=fibonocii(n-1)+fibonocii(n-2)
    return fib_mem[n]

print (fibonocii(5))
print (fibonocii(5))
print (fibonocii(6))
print (fib_mem)
