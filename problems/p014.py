l = {}
l[1] = 0
mx = -1
res = 0
for i in range(2, 1000000):
    n = i
    c = 0
    while i<=n:
        if n%2==0:
            n //= 2
        else:
            n = n * 3 + 1
        c += 1
    c += l[n]
    l[i] = c
    if mx<c:
        mx = c
        res = i
print(res)