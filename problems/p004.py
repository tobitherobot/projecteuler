prod = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        s = i*j
        if str(s)==str(s)[::-1]:
            prod = max(prod, s)
print(prod)