s = str(pow(2, 1000))
l = [(ord(x) - ord('0')) for x in s]
print(sum(l))