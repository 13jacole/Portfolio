#Finding the Nth prime number

#Using Sieve of Eratosthenes

# Taken from https://levelup.gitconnected.com/how-to-find-the-nth-prime-number-c16dac27963

def get_nth_prime(nth):
    total_primes = 0
    size_factor = 2
    s = nth*size_factor
    while total_primes < nth:
        primes = get_primes(s)
        total_primes = sum(primes[2:])
        size_factor += 1
        s = nth*size_factor
    nth_prime = count_primes(primes, nth)
    return nth_prime
    

def get_primes(s):
    primes = bytearray([1]*s)
    for i in range(2, s):
        if primes[1] == 1:
            