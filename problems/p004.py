from useful import is_palindrome

res = 0
for i in range(999, 900, -1):
    for j in range(i, 1000):
        if is_palindrome(str(i*j)):
            res = max(res, i*j)
print(res)