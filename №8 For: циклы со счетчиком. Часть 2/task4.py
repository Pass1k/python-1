a = 0
b = 10
c = 3

sum = 0
count = 0
for i in range(a, b + 1):
    if i % c == 0:
        sum += i
        count += 1

print(sum/count)