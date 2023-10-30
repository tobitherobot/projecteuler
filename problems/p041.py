import itertools

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

n = [9,8,7,6,5,4,3,2,1]

res = -1
while res<0:
    for i in itertools.permutations(n):
        if i[-1]%2!=0:
            p = int(''.join(str(x) for x in i))
            if is_prime(p):
                res = p
                break
    if res<0:
        n = n[1:]
print(res)