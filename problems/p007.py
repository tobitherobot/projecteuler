#!/bin/python3

import sys

def rwh_primes1(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1) // (2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

primes = rwh_primes1(104730)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])