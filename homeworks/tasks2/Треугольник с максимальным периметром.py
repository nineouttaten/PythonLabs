def triangle(A):
    all_sides = A
    all_sides.sort(reverse=True)
    for i in range(0, len(all_sides) - 2):
        sides = [all_sides[i], all_sides[i + 1], all_sides[i + 2]]
        if sides[1] + sides[2] > sides[0]:
            return sum(sides)
    return 0


A = list(map(lambda x: int(x), input("Введите длины отрезков через пробел: ").split(" ")))
print(triangle(A))
