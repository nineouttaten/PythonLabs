def max_palindrome(s):
    m = ""
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            string = s[j:j+i]
            if string == string[::-1]:
                m = string
    return m


s = input("Введите исходную строку: ")
print("Максимальный палиндром:", max_palindrome(s))
