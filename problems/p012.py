from math import sqrt

def count(n):
    c = 2
    root = int(sqrt(n))
    for i in range(2, root):
        if n%i==0:
            c += 2
    if root*root==n:
        c += 1
    return c

n = 1
a = 2
c = count(n)

while c<=500:
    n += a
    a += 1
    c = count(n)
print(n)
