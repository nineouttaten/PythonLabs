n = int(input())
if n % 3 == 0: # если делится на 3, то можно вставить треугольник
    k = 3
elif n % 2 != 0: # если нечетное, перебором ищем делитель
    for i in range(4, n+1):
        if n % i == 0:
            k = i
            break
        
elif n % 2 == 0 and n % 4 != 0: # если четное и не 4 ищем делитель
    for i in range(5, n):
        if n % i == 0 and i % 2 == 1:
            k = i
            break
else: # если делится на 4, то можно вставить квадрат
    k = 4
print(k)
