import sys
import numpy as np
import time
from functools import wraps

# Decorator to time functions
def timer(func):
    @wraps(func)
    def call(*args):
        start = time.time()
        x = func(*args)
        end = time.time()
        print(f'Function {func.__name__} took {end - start} seconds to complete with args: {args[0]}')
        return x
    return call


class Primes:

    @staticmethod
    def isPrime(n: int) -> bool:
        return True if sum([1 for i in range(2, int(np.sqrt(n)) + 1) if n % i == 0]) == 0 else False

    @timer
    @staticmethod
    def generatePrimes(n: int) -> list:
        primes, i = [2, 3], 3
        while (i := i + 1) <= n:
            for prime in primes:
                if i % prime == 0:
                    break
                elif prime == primes[-1]:
                    primes.append(i)
        return primes

    @timer
    @staticmethod
    def generatePrimesV2(n: int) -> list:
        primes, i = [2, 3], 3
        while (i := i + 1) <= n:
            j = 1
            while (j := j + 1) < np.sqrt(i): 
                if i % j == 0:
                    break
                elif j + 1 > np.sqrt(i):
                    primes.append(i)
        return primes

    @timer
    @staticmethod
    def generatePrimesV3(n: int) -> list:
         return [i for i in range(2,n) if Primes.isPrime(i) == True]

    @timer
    @staticmethod
    def generatePrimesV4(n: int) -> list:
        primes = [[i, True] for i in range(2,n)]
        for prime in primes:
            if prime[1] == True:
                for i in range(2*prime[0]-2,n-2,prime[0]):
                    primes[i][1] = False
        primes_real = [x[0] for x in primes if x[1] == True]
        return primes_real

    @timer
    @staticmethod
    def generatePrimesV5(n: int) -> list:
        is_prime = np.ones(n//2, dtype=bool)
        for i in range(n//2):
            if is_prime[i]: is_prime[3*i+3:n//2:2*i+3] = False
        return 2*np.nonzero(is_prime)[0][0:-1]+3


n = 10000

Primes.generatePrimes(n)
Primes.generatePrimesV2(n)
Primes.generatePrimesV3(n)
Primes.generatePrimesV4(n)
Primes.generatePrimesV5(n)

"""
@timer
def primesfrom3to(n):
    sieve = np.ones(n//2, dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    print(sieve)
    return 2*np.nonzero(sieve)[0][1::]+1
"""
