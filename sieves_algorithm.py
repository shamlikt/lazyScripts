def prime(limit):
    list2=range(2,limit)
    prime=[]
    for x in list2:
        list2=[y for y in list2 if  y%x]
        if len(list2) !=0:
            prime.append(list2.pop(0))
    return prime
 



print prime(1000)
