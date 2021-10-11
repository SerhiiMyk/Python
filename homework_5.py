# Переделать предыдущее задание с практической для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
# -каждый пункт меню должен быть методом класса(кроме exit)
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

import json


class Product:

    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __str__(self):
        return str(self.__dict__)


class Notebook:
    price_list = []

    def __init__(self):
        self.__product_list: list[Product] = []

    def create(self):
        product = input('\nwrite name ot the product: ')
        price = input('write price: ')
        self.__product_list.append(Product(product, price))
        with open('notebook.json', 'w') as file:
            json.dump(self.__product_list, file)

    @staticmethod
    def show_all():
        with open('notebook.json') as file:
            notebook_data: list[dict] = json.load(file)
            for product in notebook_data:
                print(product.get('product'), '-', product.get('price'), 'UAH')

    def sum(self):

        for i in self.__product_list:
            self.price_list.append(int(i.price))
        return sum(self.price_list)

    def max(self):

        for i in self.__product_list:
            self.price_list.append(int(i.price))
        return max(self.price_list)

    def search(self):
        search = input('enter the product name: ')
        for i in self.__product_list:
            if search == i.product:
                return i.price


notebook = Notebook()
j = 1
while j != 0:
    print('\n1) Создать запись\n'
          '2) Список все записей\n'
          '3) Общая сумма всех покупок\n'
          '4) Самая дорогая покупка\n'
          '5) Поиск по названию покупки\n'
          '6) Выход')
    select_item = int(input('\nselect a menu item: '))
    print()
    if select_item == 1:
        i = 1
        while i != 0:
            notebook.create()
            i = int(input('\nif you want to add one more item press 1 or if you want to exit press 0: '))
            if i != 1 and i != 0:
                while i != 1 or i != 0:
                    i = int(input('\nPlease press 1 or 0: '))
                    if i == 1 or i == 0:
                        break
    elif select_item == 2:
        notebook.show_all()
    elif select_item == 3:
        print('The total amount of all purchases: ', notebook.sum(), 'UAH')
    elif select_item == 4:
        print('The most expensive purchase: ', notebook.max(), 'UAH')
    elif select_item == 5:
        print('\nProduct cost: ', notebook.search(), 'UAH')
    elif select_item == 6:
        j = 0
    else:
        print('Please write a correct number of submenu!')
