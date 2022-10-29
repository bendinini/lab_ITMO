import math

def f(x, eps): # Функция вычисления ряда Тейлора для x
    n, sum = 0, 0 # n - количество просумированных членов, sum - сумма
    while 2 / ((2 * n + 1) * (x ** (2 * n + 1))) > eps:
        sum += 2 / ((2 * n + 1) * (x ** (2 * n + 1)))
        n += 1
    return sum, n

# Меню выбора задания
ans = 0
while ans != 1 and ans != 2:
    ans = int(input("Выберите задание (1, 2): "))

# 1 Задание
if ans == 1:
    R = float(input("Введите значение R: "))

    def f(x, R): # Функция из 1-й лабораторной
        # 1) Значение x в интервале [-3R; -2R]
        if -3*R <= x and x <= -2*R:
            y = math.sqrt(R**2 - (x+2*R)**2) * -1

        # 2) Значение x в интервале (-2R; -R]
        elif -2*R <= x and x <= -R:
            y = x+R

        # 3) Значение x в интервале (-R; 0]
        elif -R <= x and x <= 0:
            y = math.sqrt(R**2 - x**2)

        # 4) Значение x в интервале (0; R]
        elif 0 <= x and x <= R:
            y = R-x

        # 5) Значение x в интервале (R; 3R]
        elif R <= x and x <= 3*R:
            y = (x-R)/(R*2)*R

        return y

    dx = float((6*R)/18) # Шаг
    x = -3*R

    print(f"Интервал от {-3*R} до {3*R} с шагом {round(dx, 3)}.")
    print(f"\t  x\t\t\t  y")
    while x <= 3*R: # Интервал проверки от [-3R; 3R]
        print(f"\t{round(x, 3)}\t\t\t{round(f(x, R), 3)}")
        x += dx

# 2 Задание
else:
    x_start = float(input("Введите x (начальное): "))
    x_end = float(input("Введите x (конечное): "))
    dx = float(input("Введите шаг dx: "))
    eps = float(input("Введите точность ε: "))

    x = x_start
    print("Зн-е аргумента\tЗн-е функции\tКол-во просум. чл-в")
    while x <= x_end:
        sum, n = f(x, eps) # Воспользуемся функцией, рассчитывающая ряд Тейлора
        print(f"{round(x, 3)}\t\t\t\t{round(sum, 3)}\t\t\t\t{n}")
        x += dx # Прибавление шага к x
