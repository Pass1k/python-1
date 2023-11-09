num1 = int(input('Кубик Кости: '))
num2 = int(input('Кубик владельца: '))

if num1 >= num2:
    print(num1 + num2)
    print('Игрок платит')
else:
    print('Валделец платит')
print('Game is over')