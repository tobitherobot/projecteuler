n = 600851475143
m = 3
while 1<n:
    if n%m==0:
        n //= m
    else:
        m += 2
print(m)