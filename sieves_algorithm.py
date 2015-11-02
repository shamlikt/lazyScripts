
import sys
 
def prime(limit):
    limit=limit+1
    noprime=[False]*limit
    prime=[]
    for i in range(2,limit):
        if noprime[i]:
            continue
        else:
            for y in range(i*2,limit,i):
                noprime[y]=[True]
            prime.append(i)
    return prime
                
            
            

if __name__ == '__main__':
    print prime(int(sys.argv[1]))
