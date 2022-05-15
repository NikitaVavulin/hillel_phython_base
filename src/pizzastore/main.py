import random
from copy import deepcopy
pizzas = [
    [0, 'Греция', 370, 'Соус из томатов + помидоры + перец болгарский + лук красный + маслины + сыр Моцарелла'],
    [1, 'Маргарита', 180, 'Соус из томатов + помидоры + сыр Моцарелла'],
    [2, 'Баварская', 310, 'Соус из томатов + колбаски Баварские + бекон + помидоры + сыр Моцарелла'],
    [3, 'Барбекю', 150, 'Соус томатный + филе куриное + бекон + лук красный + сыр Моцарелла + соус BBQ'],
    [4, 'С ветчиной и сыром', 260, 'Соус из томатов + ветчина + сыр Моцарелла'],
    [5, 'Деревенская', 400, 'Соус из томатов + колбаски Мюнхенские + салями + огурцы солёные + сыр Моцарелла'],
    [6, 'Чикаго', 330, 'Соус из томатов + куриное филе + бекон + перец болгарский + лук красный + сыр Моцарелла'],
    [7, '4 Сыра', 240, 'Соус из томатов + куриное филе + сыры: Моцарелла, Эдам, Пармезан, Дор Блю'],
    [8, 'Папперони', 170, 'Соус из томатов + пепперони + сыр Моцарелла'],
    [9, 'С грибами', 190, 'Соус из томатов + ветчина + шампиньоны + маслины + сыр Моцарелла']
]

while True:
    a = input("Введите:\n1 для вывода пицц\n2 для вывода рандомных пицц\n0 для очистки\n3 для вывода пицц дешевле и дороже 250грн:")
    match a:
        case '0':
            break
        case '1':
            print(pizzas)
        case '2':
            rd1 = random.randint(1, 5)
            rd2 = random.sample(pizzas, rd1)
            print(rd1)
            print(rd2)

        case '3':
            pizzas2 = [item for item in pizzas if item[2] <= 250]
            print(pizzas2)
            pizzas3 = [item for item in pizzas if item[2] >= 250]
            print(pizzas3)



        case _:
            print("Не верно, введите указаное число")