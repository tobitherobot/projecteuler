a = 1
b = 1
n = 2
while len(str(a))<1000:
    c = a+b
    b = a
    a = c
    n += 1
print(n)