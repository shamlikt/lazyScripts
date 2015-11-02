import sys

def prime(limit):
    list2=range(3,limit,2)
    prime=[];prime.append(2)
    while len(list2):
        primeD=(list2.pop(0))
        prime.append(primeD)
        list2=[x for x in list2 if x-(x/primeD)*primeD]
    return prime
        


       

if __name__ == '__main__':
    print prime(int(sys.argv[1]))
