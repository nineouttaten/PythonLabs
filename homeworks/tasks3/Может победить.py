def max_smaller(letter, A):
    max = " "
    for char in A:
        if char <= letter and char > max:
            max = char
    return max


def can_Win(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    for i in range(len(list1)):
        if max_smaller(list1[i], list2) != " ":
            list2.remove(max_smaller(list1[i], list2))
        else:
            return False
    return True




s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
if can_Win(s1, s2):
    print("Строка \"{}\" может победить строку \"{}\":".format(s1, s2))
elif can_Win(s2, s1):
    print("Строка \"{}\" может победить строку \"{}\":".format(s2, s1))
else:
    print("Нет такой перестановки")
