#!/bin/python3

import sys

t = int(input().strip())
s = set()
for i in range(100, 1000):
        for j in range(i, 1000):
            if 101101 <= i*j and len(str(i*j))==6 and str(i*j)==str(i*j)[::-1]:
                s.add(i*j)
l = list(s)

for a0 in range(t):
    n = int(input().strip())
    l.append(n)
    l.sort()
    res = l[l.index(n)-1]
    print(res)

''' 

100 <= a <= b < 1000
101101 <= n <= 906609

-> only 279 different in possible range

'''