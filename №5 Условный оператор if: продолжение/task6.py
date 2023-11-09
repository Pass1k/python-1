price = int(input('Введите цену: '))
size = int(input('Введите площадь: '))

if size >= 100 and price <= 10:
    print('Good')
elif size >= 80 and price <= 7:
    print('Good')
else:
    print('Not good')