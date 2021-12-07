a = 1
b = 1
sum = 0
while a<4000000:
    if a%2==0:
        sum += a
    c = a+b
    b = a
    a = c
print(sum)