months = [31,28,31,30,31,30,31,31,30,31,30,31]
first = 1
year = 1900
count = 0
while year<=2000:
    leap = year%400==0 or (year%100!=0 and year%4==0)
    for i in range(12):
        if leap and i==1:
            first += 29
        else:
            first += months[i]
        first %= 7
        if first==0 and 1901<=year and year<=2000:
            count += 1
    year += 1
    first %= 7
print(count)
