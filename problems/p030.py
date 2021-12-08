a = []
for i in range(3, 1000000):
    sm = 0
    n = i
    while 0<n and sm<=i:
        sm += (n%10)**5
        n //= 10
    if sm==i:
        a.append(i)
print(sum(a))