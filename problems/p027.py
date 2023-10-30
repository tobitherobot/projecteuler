from useful import is_prime

res = -1
mx = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        c = 0
        while is_prime(abs(n**2 + a*n + b)):
            c += 1
            n += 1
        if mx<c:
            mx = c
            res = a*b
print(res)