a = int(input('Введите а: '))
b = int(input('Введите b: '))

count = 0
sum = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        sum += i

if count > 0:
    avg = sum / count
    print(f"Среднее арифметическое всех чисел от {a} до {b}, кратных 3, равно {avg:.2f}")
else:
    print("В указанном интервале нет чисел, кратных 3.")