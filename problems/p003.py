#!/bin/python3

import sys

def is_prime(n):
    if n<3:
        if n==2:
            return True
        else:
            return False
    elif n%2==0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def get_smallest_factor(n):
    if is_prime(n):
        return n
    elif n%2==0:
        return 2
    else:
        m = 3
        while n%m!=0:
            m += 2
        return m

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    f = 1
    while n > 1:
        f = get_smallest_factor(n)
        while n%f == 0:
            n //= f
    print(f)