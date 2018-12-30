"""
sum of primes below 2 million

miller rabin test
a = 31, 73

make n into n-1
divide n-1 by 2 until it wont divide evenly, record num of divisions
leftover multiplier is d
num of divisions is s

if a^d != 1 mod n
and a^2rd != -1 mod n  repeated where r is all possibilities from 1 to s-1
then n not prime

generate prime down list with prime tests built in
generate prime up list with prime tests built in
merge lists
"""

import time
import math

def divcounter (num):
    count = 0
    while num%2 == 0:
        count += 1
        num /= 2
    #print('dividing ',num*2**count,' and count is ',count)
    return count

def primetest(ugh):
    #print ('now prime testing ',ugh)
    s = divcounter(ugh-1) #the number of even divides by two
    #print(type(s))
    d = int((ugh-1) / 2**s) #the remaining multiplier after div two
    #print(type(d))
    #print ('s= ',s,' and d= ',d)
    result = True
    if 2**d%ugh != 1 and 3**d%ugh != 1 and 5**d%ugh != 1: #true if not prime
        for r in range (s):#ends before the end of s-1
            f = d*2**r
            g = ugh-1
            if (2**(f)%ugh) != (g) and (3**(f)%ugh) != (g) and (5**(f)%ugh) != (g):
                #print('using ', r,', ',2**(d*2**r)%ugh, ' and ',3**(d*2**r)%ugh,' and ',5**(d*2**r)%ugh,' should not be ', ugh-1)
                result = False
            else:
                #print('prime using ', r,', ',2**(d*2**r)%ugh, ' and ',3**(d*2**r)%ugh,' and ',5**(d*2**r)%ugh,' should not be ', ugh-1)
                result = True
                break
    #print(ugh, ' is ', result)
    return result
    

start = time.time()
m = 2000000
a = [2, 3, 5]
b = [6*n-1 for n in range(2, int((m+1)/6)+1) if primetest(6*n-1) == 1] #start at 2
c = [6*n+1 for n in range(1, int((m-1)/6)+1) if primetest(6*n+1) == 1] #start at 1
end = time.time()
print(sum(a+b+c))
print('total time: ',end - start)
exit()

    
            
