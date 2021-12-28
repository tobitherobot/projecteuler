#!/bin/python3

import sys

sm = 0
sqr = 0
diff = []
for i in range(1, 10001):
    sm += int(pow(i, 2))
    sqr += i
    diff.append(sqr*sqr - sm)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(diff[n-1])