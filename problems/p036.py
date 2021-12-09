def is_palindrome(n):
    s = str(n)
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

sm = 0
for i in range(1000000):
    if is_palindrome(i) and is_palindrome(str(bin(i))[2:]):
        sm += i
print(sm)