a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
D = (b ** 2) - (4 * a * c)
print("Дискриминант равен ", D)
if D < 0:
    print("Действительных корней нет")
    x1 = (-b + (D ** (1 / 2))) / (2 * a)
    x2 = (-b - (D ** (1 / 2))) / (2 * a)
    print("Первый корень в виде комплексного числа ", x1)
    print("Второй корень в виде комплексного числа ", x2)

elif D == 0:
    x = -b / (2 * a)
    print("Уравнение имеет один корень: ", x)

else:
    x1 = (-b + (D ** (1 / 2))) / (2 * a)
    x2 = (-b - (D ** (1 / 2))) / (2 * a)
    print("Первый корень уравнения ", x1)
    print("Второй корень уравнения ", x2)
