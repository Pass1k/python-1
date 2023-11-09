a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

if a > b:
    max = a
else:
    max = b
if c > max:
    max = c

print(max)