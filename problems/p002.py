#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    a = 1
    b = 1
    sum = 0
    while a<n:
        if a%2==0:
            sum += a
        c = a+b
        b = a
        a = c
    print(sum)