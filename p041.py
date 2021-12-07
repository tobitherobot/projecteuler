import itertools
from useful import is_prime

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
