def pair_sum1(arr,k):
    arr=sorted(arr)
    max_val=abs(arr[0]-k)
    print (max_val)
    for i in arr:
        if arr[i]==max_val:
            break
        else:
            continue
    print (i)
    for j in range(int(i/2)):
        print ("{0},{1}".format(arr[j],arr[i-j]))

print (pair_sum1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print (pair_sum1([1,2,3,1],3))
#print (sorted([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1]))
