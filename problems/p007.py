primes = [2]
n = 3

while len(primes)<10001:
    flag = True
    for p in primes:
        if n%p==0:
            flag = False
            break
    if flag:
        primes.append(n)
    n += 2
print(primes[-1])