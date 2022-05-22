import random
from collections import namedtuple


Pizza = namedtuple('Pizza', ['idx', 'name', 'price', 'description'])
Pizzas = [
    Pizza(0, 'Греция', 370, 'Соус из томатов + помидоры + перец болгарский + лук красный + маслины + сыр Моцарелла'),
    Pizza(1, 'Маргарита', 180, 'Соус из томатов + помидоры + сыр Моцарелла'),
    Pizza(2, 'Баварская', 310, 'Соус из томатов + колбаски Баварские + бекон + помидоры + сыр Моцарелла'),
    Pizza(3, 'Барбекю', 150, 'Соус томатный + филе куриное + бекон + лук красный + сыр Моцарелла + соус BBQ'),
    Pizza(4, 'С ветчиной и сыром', 260, 'Соус из томатов + ветчина + сыр Моцарелла'),
    Pizza(5, 'Деревенская', 400, 'Соус из томатов + колбаски Мюнхенские + салями + огурцы солёные + сыр Моцарелла'),
    Pizza(6, 'Чикаго', 330, 'Соус из томатов + куриное филе + бекон + перец болгарский + лук красный + сыр Моцарелла'),
    Pizza(7, '4 Сыра', 240, 'Соус из томатов + куриное филе + сыры: Моцарелла, Эдам, Пармезан, Дор Блю'),
    Pizza(8, 'Папперони', 170, 'Соус из томатов + пепперони + сыр Моцарелла'),
    Pizza(9, 'С грибами', 190, 'Соус из томатов + ветчина + шампиньоны + маслины + сыр Моцарелла')
]
def error():
    print("Не верно, введите указаное число!")

def intro():
    print("Введите:\n0 для очистки\n1 для вывода пицц\n2 для вывода рандомных пицц\n3 для вывода пицц дешевле и дороже 250грн:")

def pizzalist(li):
    for item in li:
        print("\nНазвание:", item.name, "\nЦена:", item.price, "\nОписание:", item.description)

def randompizza(li):
    rd1 = random.randint(1, 5)
    rd2 = random.sample(li, rd1)
    print("\nКоличество рандомных пицц:", rd1, "\nПиццы:")
    for item in rd2:
        print("\nНазвание:", item.name, "\nЦена:", item.price, "\nОписание:", item.description)

def filtpizza(li):
    pizzas2 = [item for item in li if item.price <= 250]
    pizzas3 = [item for item in li if item.price >=250]
    print("Пиццы дешевле 250грн: ")
    for item in pizzas2:
        print("\nНазвание:", item.name, "\nЦена:", item.price, "\nОписание:", item.description)
    print("\nПицы дороже 250грн:")
    for item in pizzas3:
        print("\nНазвание:", item.name, "\nЦена:", item.price, "\nОписание:", item.description)


while True:
    intro()
    a = input()
    match a:
        case '0':
            break
        case '1':
            print(pizzalist(Pizzas))
        case '2':
            print(randompizza(Pizzas))

        case '3':
            print(filtpizza(Pizzas))

        case _:
            print(error())