pos_num = 0
neg_num = 0

while True:
    scroll = int(input('Введите оценку: '))
    if scroll > 0:
        pos_num += 1
    elif scroll < 0:
        neg_num += 1
    else:
        break

print('Кол-во положительных чисел:', pos_num)
print('Кол-во отрицательных чисел:', neg_num)