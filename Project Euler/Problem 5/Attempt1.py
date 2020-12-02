#Initial Idea -- Prime Factors

#All numbers can be expressed as a product of their prime factors
#If we apply prime factorization to each number from 1-20, and multiply the factors, we should find the smallest numjber that is a evenly divisible by all numbers 1-20.

import math

#prime numbers -- brute force because only 1-20
def BrutegeneratePrimes(upperlimit):
    primes = [2]
    for i in range(3, upperlimit+1, 2):
        isPrime = True
        for j in range(2, i, 1):
            if i%j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes

############
primes = BrutegeneratePrimes(20)
print(primes)
result = 1
exp = []

for p in range(0, len(primes), 1):
    exp.append(math.floor(math.log(20)/math.log(primes[p])))

for q in range(0, len(primes), 1):
    result = result * (primes[q]**exp[q])
    
print(result)