from useful import is_prime
from math import log10

res = 1
n = 3
while n<1000000:
    x = n
    s = str(x)
    least = True
    for i in range(1, len(s)):
        if int(s[0])>int(s[i]):
            least = False
            break
    if least and is_prime(x):
        count = 1
        flag = True
        while True:
            x = pow(10, int(log10(n))) * (x%10) + x//10
            if x==n:
                break
            elif not is_prime(x) or x<n:
                flag = False
                break
            else:
                count += 1
        if flag:
            res += count
    n += 2
print(res)