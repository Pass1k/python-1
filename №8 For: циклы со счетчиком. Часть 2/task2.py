count = 10
sum = 0

for i in range(0, count, 5):
    print(f"Должник с номером {i}")
    sum += int(input(f'Сколько должны? '))

print(f'Общая сумма долга:{sum}')