def get_list_of_diagonal_elements(matrix, start_line, start_row):
    x, y = start_row, start_line
    lst = [[matrix[y][x], y, x]]
    while x + 1 < rows and y + 1 < lines:
        x += 1
        y += 1
        lst.append([matrix[y][x], y, x])
    return lst

lines = int(input("Введите количество строк в матрице: "))
rows = int(input("Введите количество столбцов в матрице: "))
matrix = []
print("Заполните матрицу")
for i in range(lines):
    matrix.append([])
    print("{} строка".format(i))
    for j in range(rows):
        matrix[i].append(int(input("{} столбец: ".format(j))))
print("Ваша матрица: ")
for line in matrix:
    print(line)
# Сортировка по 1 столбцу
for i in range(lines):
    lst = get_list_of_diagonal_elements(matrix, i, 0)
    values = []
    for j in range(len(lst)):
        values.append(lst[j][0])
    values.sort()
    y = i
    x = 0
    k = 0
    while x + 1 < rows and y + 1 < lines:
        matrix[y][x] = values[k]
        x += 1
        y += 1
        k += 1
    matrix[y][x] = values[k]
# Сортировка по 1 строке
for i in range(rows):
    lst = get_list_of_diagonal_elements(matrix, 0, i)
    values = []
    for j in range(len(lst)):
        values.append(lst[j][0])
    values.sort()
    y = 0
    x = i
    k = 0
    while x + 1 < rows and y + 1 < lines:
        matrix[y][x] = values[k]
        x += 1
        y += 1
        k += 1
    matrix[y][x] = values[k]


print("Результирующая матрица:")
for line in matrix:
    print(line)
