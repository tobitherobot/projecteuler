res = -1
mx = 0

def is_prime(n):
    if n<3:
        if n==2:
            return True
        else:
            return False
    elif n%2==0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

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