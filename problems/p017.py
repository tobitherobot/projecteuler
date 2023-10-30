# (zero) one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
ones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
# (zero) (ten) twenty thirty forty fifty sixty seventy eighty ninety
tens = [0,0,6,6,5,5,5,7,6,6]

def count(n):
    c = 0
    if 100<=n:
        c += ones[n//100]
        c += 0 if n%100==0 else 3 # and
        c += 7 # hundred
    if n%100<20:
        c += ones[n%100]
    else:
        c += tens[(n%100) // 10]
        c += ones[n%10]
    return c

c = 11 # one thousand
for i in range(1, 1000):
    c += count(i)
print(c)   