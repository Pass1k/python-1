buy1 = int(input('Введит стоимость: '))
buy2 = int(input('Введит стоимость: '))
buy3 = int(input('Введит стоимость: '))

sum = buy1 + buy2 + buy3
if sum > 10_000:
    sum -= sum * 10 / 100
    print('Итогавая сумма:', int(sum))
else:
    print('Итогавая сумма:', sum)