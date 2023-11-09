n = int(input('Введите количество карточек: '))

sum = 0
for i in range(1, n + 1):
    sum += i

for i in range(1, n):
    left = int(input('Введите номер оставшейся карточки: '))
    sum -= left 

print('Номер пропавшей карточки:', sum)