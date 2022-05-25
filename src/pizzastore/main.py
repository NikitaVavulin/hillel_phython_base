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
def decor_str(func):
    def inner(e):
        func(e)
        print('-' * 100)
    return inner

def decor_list(func):
    def inner(s):
        print('*' * 100)
        func(s)
        print("Количество пицц в списке:", len(s))
        print('*' * 100)
    return inner

def decor_check(func):
    def inner(k):
        print(f'\n{"Чек:"}')
        print('*' * 100)
        all = func(k)
        print('*' * 100)
        print(f'Цена за всё:{all}')
        print('*' * 100)
    return inner

def error():
    print("Не верно, введите указаное число!")

def intro():

    print("Введите:\n0 для очистки\n1 для вывода пицц\n2 для вывода рандомных пицц\n3 для вывода пицц дешевле и дороже 250грн:")

@decor_list
def pizzalist(li):
    for item in li:
        print_str(item)

@decor_str
def print_str(item):
    print(f'{item.idx + 1}, Название: {item.name}, Цена: {item.price}')
    print(f'Описание: {item.description}')

@decor_check
def check(li):
    i = 0
    for nm, unit in enumerate(li, start=1):
        q = random.randint(1, 3)
        t = unit.price * q
        i += t
        print(f'{nm} | Название: {unit.name} | Цена: {unit.price} | Количество: {q} | Полная цена:{t}')

    return i


while True:
    intro()
    a = input()
    match a:
        case '0':
            break
        case '1':
            print(pizzalist(Pizzas))
        case '2':
            pizza_random = random.sample(Pizzas, k = random.randint(1, 5))
            check(pizza_random)

        case '3':
            pizzas2 = [item for item in Pizzas if item.price <= 250]
            pizzas3 = [item for item in Pizzas if item.price >= 250]
            print('\nПиццы дешевле 250: ')
            pizzalist(pizzas2)
            print('\nПиццы дороже 250: ')
            pizzalist(pizzas3)

        case _:
            print(error())