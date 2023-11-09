hours = int(input('Введите отработанные часы: '))
kredit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))

income = 200 * hours / 2**3 + hours

if income >= kredit + food:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')