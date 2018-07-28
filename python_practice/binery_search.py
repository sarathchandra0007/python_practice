def binery_search(s,ele):
    middle=len(s)//2


    if ele==s[middle]:
        return True
    else:
        if ele>middle:
            return binery_search(s[middle+1:],ele)
        else:
            return binery_search(s[:middle],ele)




print (binery_search([1,2,3,4,5,6,7,8,9,10],10))
