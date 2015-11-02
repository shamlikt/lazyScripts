#prime factorization using sieves algorithms


def prime_gen(limit):
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


     
def fact_gen(number,primes):
   factor=[]
   if number==primes.pop():
       factor.append(number)
       return factor
   while number !=1 :
       for i in primes:
           if not number%i:
               factor.append(i)
               number=number/i
               break
   return factor

       


if __name__=='__main__':
    number=input()
    primes= prime_gen(number)
    print  fact_gen(number,primes)
