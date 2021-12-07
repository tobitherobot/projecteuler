import itertools

n = [0,1,2,3,4,5,6,7,8,9]
c = 0
for m in itertools.permutations(n):
    c += 1
    if c==1000000:
        print(''.join(str(x) for x in m))
        break
