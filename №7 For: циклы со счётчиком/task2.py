# Создаем переменную для хранения суммы зарплаты за год
total_salary = 0

# Проходим по каждому месяцу и запрашиваем зарплату от пользователя
for month in range(1, 13):
    salary = float(input(f"Введите зарплату за {month}-й месяц: "))
    total_salary += salary

# Вычисляем среднюю зарплату за год
average_salary = total_salary / 12

# Выводим результат на экран
print(f"Средняя зарплата за год: {average_salary}")
