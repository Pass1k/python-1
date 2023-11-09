x = int(input("Введите число х: "))

# для X > 0, Y = X − 12
# для X = 0,  Y = 5
# для X < 0, Y = X2

if x > 0:
    y = x - 12
    print('Y is equal to', y)
elif x == 0:
    y = 5
    print('Y is equal to', y)
else:
    y = x ** 2
    print('Y is equal to', y)