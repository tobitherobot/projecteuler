from math import gcd

f = [1, 1]
for n in range(12, 100):
    for d in range(n+1, 100):
        if n%10!=0 and n%11!=0 and d%10!=0 and d%11!=0:
            if str(n)[0]==str(d)[0]:
                a = int(str(n)[1])
                b = int(str(d)[1])
            elif str(n)[0]==str(d)[1]:
                a = int(str(n)[1])
                b = int(str(d)[0])
            elif str(n)[1]==str(d)[0]:
                a = int(str(n)[0])
                b = int(str(d)[1])
            elif str(n)[1]==str(d)[1]:
                a = int(str(n)[0])
                b = int(str(d)[0])
            else:
                continue
            
            g1 = gcd(n, d)
            g2 = gcd(a, b)
            if n/g1==a/g2 and d/g1==b/g2:
                f[0] *= a
                f[1] *= b
print(f[1] // gcd(f[0], f[1]))