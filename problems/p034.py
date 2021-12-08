from math import factorial

n = 3
res = 0
while n<100000:
    x = n
    sm = 0
    while 0<x:
        sm += factorial(x%10)
        x //= 10
    if sm==n:
        res += n
    n += 1
print(res)