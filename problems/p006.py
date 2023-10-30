sm = 0
sqr = 0
for i in range(1, 101):
    sm += int(pow(i, 2))
    sqr += i
print(int(pow(sqr, 2)) - sm)