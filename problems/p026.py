f = -1
l = 0
for i in range(2, 1001):
    divs = []
    n = 1
    while n not in divs:
        if n%i==0:
            divs.clear()
            break
        elif n//i==0:
            n *= 10
        else:
            divs.append(n)
            n %= i
    if 0<len(divs):
        length = len(divs)-divs.index(n)
        if l<length:
            f = i
            l = length
print(f)
