r = 1
last = 1
diff = 2
sm = 1

while r<1001:
    for i in range(4):
        last += diff
        sm += last
    r += 2
    diff += 2
print(sm)