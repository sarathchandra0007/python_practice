def countways(n):
    arr=[0]*(n+1)
    arr[0]=1
    arr[1]=1
    arr[2]=2

    for i in range(3,n+1):
        arr[i]=arr[i-3]+arr[i-2]+arr[i-1]
    return arr[n]

n=4
print (countways(n))

