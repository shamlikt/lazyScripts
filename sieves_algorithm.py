def prime(limit):
    list2=range(2,limit)
    prime=[]
    while len(list2):
        primeD=(list2.pop(0))
        prime.append(primeD)
        list2=[x for x in list2 if x-(x/primeD)*primeD]
    return prime
        




print prime(1000)
