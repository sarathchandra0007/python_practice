

def coin_exchange(amount,coins,known_mem):

    max_val=amount

    if amount in coins:
        known_mem[amount]=1
        return known_mem[amount]
    elif known_mem[amount]>0:
        return known_mem[amount]
    else:
        for i in [c for c in coins if c<amount]:
            sum_val=1+coin_exchage(amount-i,coins,known_mem)

            if sum_val<max_val:
                max_val=sum_val
            known_mem[amount]=min_coins

    return min_coins



amount=74
coins=[1,5,10,25]
known_mem=[0]*73
print (coin_exchange(amount,coins,known_mem))
#print (known_mem)
