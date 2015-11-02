

def prime_gen(limit):
    list2=range(3,limit+1,2)
    prime=[];prime.append(2)
    while len(list2):
        primeD=(list2.pop(0))
        prime.append(primeD)
        list2=[x for x in list2 if x-(x/primeD)*primeD]
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

       
         
num=input()
primes= prime_gen(num)

print  fact_gen(num,primes)
