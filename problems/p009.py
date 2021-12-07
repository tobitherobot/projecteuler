res = -1
for a in range(334):
    for b in range(a, 501):
        c = 1000-a-b
        if a*a+b*b==c*c:
            res = a*b*c
            break
    if 0<res:
        break
print(res)