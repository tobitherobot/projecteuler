import math

def sum_of_divisors(n):
    sqr = math.sqrt(n)
    sum = 1
    for i in range(2, int(sqr)):
        if n%i==0:
            sum += i + n//i
    return sum

sum = 0
for i in range(2, 10001):
    a = sum_of_divisors(i)
    if i<a and sum_of_divisors(a)==i:
        print(str(i) + " " + str(a))
        sum += i + a
print(sum)