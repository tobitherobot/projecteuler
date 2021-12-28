#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fac = {}

    for i in range(1, n+1):
        n = i
        d = 2
        while n!=1:
            c = 0
            while n%d==0:
                n //= d
                c += 1
            if 0<c:
                if d in fac:
                    fac[d] = max(fac[d], c)
                else:
                    fac[d] = c
            d += 1
    prod = 1
    for f in fac:
        prod *= int(pow(f, fac[f]))
    print(prod)