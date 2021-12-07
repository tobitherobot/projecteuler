fac = 1
for i in range(2, 101):
    fac *= i
sum = 0
for c in str(fac):
    sum += int(c)
    print(int(c))
print(sum)
