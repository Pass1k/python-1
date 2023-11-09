print('Начался восьмичасовой рабочий день.')
i = 1
total = 0
shop = 0

while i <= 3:
    print(f'{i}-й час')
    task = int(input('Сколько задач решит Максим: '))
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    shop += call
    total += task
    i += 1

print(f'Рабочий день закончился. Всего выполнено задач: {total}')
if shop > 0:
    print('Нужно зайти в магазин.')