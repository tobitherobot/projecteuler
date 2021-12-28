#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    m = (n-1) // 15
    sum = m*60 + (((m-1)* m)// 2) * 105
    for i in range(m*15+1, n):
        if i%3==0 or i%5==0:
            sum += i
    print(sum)



'''

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ...
- - x - x x - - x x  -  x  -  -  x  | -  -  x  -  x  x  -  -  x  x  -  x  -  -  x  -  ...
            = 3+5+6+9+10+12+15 = 60 | = 60 + 7*15

f(45) = 60  +  60+1*105  +  60+2*105
repeating pattern after 15 numbers: n = inp // 15 (45 -> 3)

f(n) = n*60  +  (1*105 + 2*105 + ... + (n-1)*105)
    = n*60 + (((n-1) * (n-1+1)) // 2) * 105
    = n*60 + (((n-1)* n)// 2) * 105

'''