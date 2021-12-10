with open("resources/words.txt") as f:
    words = f.readline().strip().replace("\"", "").split(",")

t = []
sm = 0
a = 1
while sm<520:
    sm += a
    t.append(sm)
    a += 1

count = 0
for w in words:
    sm = 0
    for c in w:
        sm += ord(c) - ord('A') + 1
    if sm in t:
        count += 1
print(count)