num = int(input('Введите четерехзначное число: '))

num_1 = num // 1000
num_2 = (num // 100) % 10
num_3 = (num // 10) % 10
num_4 = num % 10

print(num_1)
print(num_2)
print(num_3)
print(num_4)