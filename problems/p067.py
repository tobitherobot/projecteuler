with open("resources/triangle.txt") as f:
    input = [[int(x) for x in z.strip().split(" ")] for z in f.readlines()]

for i in range(len(input)-1, -1, -1):
    for j in range(len(input[i])-1):
        input[i-1][j] += max(input[i][j], input[i][j+1])
print(input[0][0])