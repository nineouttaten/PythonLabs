  
def concatenation(s):
    L = len(s)
    k = 0
    parts = []
    for i in range(2, L, 2):
        for j in range(L - i + 1):
            word = s[j:j + i]
            part1 = word[:i // 2]
            part2 = word[i // 2:]
            if part1 == part2 and not part1 in parts:
                parts.append(part1)
                k += 1
    return k


a = input("Введите исходную строку: ")
print(concatenation(a))
