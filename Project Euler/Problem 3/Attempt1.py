
## THIS DOES NOT WORK -- Memory error when creating prime[] list (line 10)

#Sieve of Eratosthenes - https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def SieveOfEratosthenes(n): 
    primeArray = []
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            primeArray.append(p)
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Create list of prime numbers
    return primeArray
    

def main():
    num = 600851475143
    print("Creating list of primes...")
    Primes = SieveOfEratosthenes(num)
    print("Removing non-factors...")
    for p in Primes:
        if num%p != 0:
            Primes.remove(p)
    
    print("The greated prime factor of " + str(num) + " is: " + str(max(Primes)))


main()