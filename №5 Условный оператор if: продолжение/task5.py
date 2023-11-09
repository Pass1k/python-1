a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

if a == b == c:
    print('все совпадают')
elif a == b or a == c or c == b:
    print('Два числа совпадает')
else:
    print('Все разные')