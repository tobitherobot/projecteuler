n = 600851475143
div = 3
while n > 1:
    if n % div == 0:
        n = n // div
    else:
        div += 2
print(div)