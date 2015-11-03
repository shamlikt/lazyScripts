#prime factorization using sieves algorithms


def prime_gent(limit):
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

       

def hcf(data):
    data[0]=int(data[0]);data[1]=int(data[1])
    dic={};sum=1
    fact1=fact_gen(data[0],prime_gent(data[0]))
    fact2=fact_gen(data[1],prime_gent(data[1]))
    common=set(fact1).intersection(set(fact2))
    for x in common:
        dic[x]=min(fact1.count(x),fact2.count(x))
    
    for key in dic:
        sum=sum*(key**dic[key])
    return sum
    



print hcf(raw_input("Give 2 input seperate by comma: ").split(","))
