def not_zero(array):
    for char in array:
        if char != 0:
            return True
    return False

def compare(i, j):
    s1 = str(i)
    s2 = str(j)
    if int(s1 + s2) > int(s2 + s1):
        return 1
    else:
        return -1

numbers = list(map(int, input("Введите числа через пробел: ").split(" ")))
if not_zero(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1, i, -1):
            if (compare(numbers[i], numbers[j]) != 1):
                numbers[i], numbers[j] = numbers[j], numbers[i]

    result = ""
    for i in numbers:
        result = result + str(i)

    print("Самое большое число, которое может получиться:", result)
else:
    print("Самое большое число, которое может получиться: 0")
