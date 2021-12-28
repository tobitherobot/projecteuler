#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n, k = map(int, input().strip().split(' '))
    num = input().strip().split('0')
    mx = 0
    
    for s in num:
        n = len(s)
        prod = 1
        if n < k:
            continue
        for i in range(k):
            prod *= int(s[i])
        mx = max(mx, prod)
        for i in range(n-k):
            prod = prod // int(s[i]) * int(s[i+k])
            mx = max(mx, prod)
    print(mx)