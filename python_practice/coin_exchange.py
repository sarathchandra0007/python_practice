def rec_coin(target,coins):
    
    min_num=target

    if target in coins:
        return 1
    
    else:
        for i in [c for c in coins if c<=target]:
            print (i)
            print (target-i)
            sum_coins=1+rec_coin(target-i,coins)
            print ("hi")
            if min_num>sum_coins:
                min_num=sum_coins
    return min_num
print (rec_coin(15,[1,5,10]))
