sum = 0
sqr = 0
for i in range(1, 101):
    sum += int(pow(i, 2))
    sqr += i
sqr = int(pow(sqr, 2))
print(sqr-sum)