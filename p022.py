with open("resources/names.txt") as f:
    names = f.readline().replace("\"", "").split(",")

names.sort()
res = 0
for name in names:
    sum = 0
    for c in name:
        sum += ord(c)-ord('A')+1
    res += sum * (names.index(name)+1)
print(res)