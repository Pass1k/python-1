n = int(input('Введите количество школьников:'))

perfect = 0 
good = 0
bad = 0

for i in range(1, n+1):
    cheack = int(input('Сколько получил: '))
    if cheack == 5:
        perfect += cheack
    elif cheack == 4:
        good += cheack
    elif cheack == 3:
        bad += cheack
    else:
        print('Вы вели не правильную оценку')

if good < perfect > bad:
    print('оличников сегодня больше')
elif perfect < good > bad:
    print('Хорошистов сегодня больше')
else:
    print('Тройшников больше')