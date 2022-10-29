# Задание матрицы с клавиатуры:
# n, m = map(int, input("Введите размер матрицы n*m: ").split())
# print("Введите матрицу")
# a = []
# for i in range(n):
#     a.append([int(j) for j in input().split(' ', m - 1)])

# Задание матрицы напрямую:
a = [[7, 2, 3, -1],
     [4, -2, 10, -1],
     [7, 8, 1, 0]]
n = len(a)
m = len(a[0])

# n - количество строчек, m - количество столбцов

all_elements = [] # одномерный массив, хранящий все элементы матрицы
zero_string = 0 # количество строк, не содержащих ни одного нулевого элемента
for i in range(n):
    count = 0 # счетчик элементов-нулей
    for j in range(m):
        if a[i][j] != 0:
            count += 1
        all_elements.append(a[i][j]) # добавление каждого элемента в all_elements

    if count == m: # если количество ненулевых элементов = количество элементов в строке -> строка не содержит нулевые элементы
        zero_string += 1

print("Количество строк, не содержащих ни одного нулевого элемента:", zero_string)

all_elements.sort(reverse = True) # Сортировка по убыванию в целях удобства использования в цикле
checkpoint = True # Чекпоинт: был ли выведен ответ? Изначально - чекпоинт активирован (True)
for i in range(1, n*m):
    if all_elements[i] == all_elements[i-1]: # Сравнение соседствующих элементов (есть ли же такой элемент дважды в матрице?)
        print("Максимальное из чисел, встречающихся в заданной матрице более одного раза:", all_elements[i])
        checkpoint = False # Ответ выведен -> чекпоинт деактивирован
        break

if checkpoint:
    print("Не нашлось максимального из чисел, встречающихся в заданной матрице более одного раза.")