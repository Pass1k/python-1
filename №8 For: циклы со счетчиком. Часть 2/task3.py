time = 3
answer = 0

for i in range(time, 0, -1):
    answer = int(input('1-стоп, 2-продолжать: '))
    if answer == 1:
        print('Ваша еда готова, можете забрать')
        break
    else:
        print(f'Осталось {i} секунд')
else:
    print('Ваша еда готова, можете забрать2')


        