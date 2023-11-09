start = 2
stop = -2
step = -1

for x in range(start, stop-1, step):
    y = x**3 + 2 * x**2 - 4  * x + 1
    print(f'В точке {x} функция равна {y}')
    