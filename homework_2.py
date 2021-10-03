# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################

# st = input('type the string: ')
#
# for i in range(len(st)):
#     if st[i].isdigit():
#         if i == len(st) - 1:
#             print(st[i])
#         else:
#             print(st[i], end=', ')

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################

# st = input('type the string: ')
# for i in range(len(st)):
#     if st[i].isdigit():
#         print(st[i], end='')
#     elif st[i] == ' ' and st[i-1].isdigit():
#         print(', ', end='')

# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# greeting = greeting.upper()
# #
# list = [greeting[i] for i in range(len(greeting))]
# print(list)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# list = [i ** 2 for i in range(0, 50) if i % 2 != 0]
# print(list)

# function
#
# - створити функцію яка виводить ліст

# def func_1(*args):
#     l = []
#     for i in range(len(args)):
#         l.append(args[i])
#     print(l)
#
#
# func_1(1, 2, 3, 4)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.

# def func_2(a, b, c):
#     if a < b and a < c:
#         print(a)
#         return a
#     elif b < a and b < c:
#         print(b)
#         return b
#     else:
#         print(c)
#         return c
#
#
# res = func_2(1, 2, 3)
# print(res)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def func_3(a, b, c):
#     if a > b and a > c:
#         print(a)
#         return a
#     elif b > a and b > c:
#         print(b)
#         return b
#     else:
#         print(c)
#         return c
#
#
# res = func_3(1, 2, 3)
# print(res)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def func_4(*args):
#     l = []
#     for i in range(len(args)):
#         l.append(args[i])
#     print(max(l))
#     return min(l)
#
#
# res = func_4(1, 2, 3)
# print(res)


# - створити функцію яка виводить ліст

# def func_5(*args):
#     l = []
#     for i in range(len(args)):
#         l.append(args[i])
#     print(l)
#
#
# func_5(1, 2, 3, 4)

# - створити функцію яка повертає найбільше число з ліста

# def func_6(*args):
#     l = []
#     for i in range(len(args)):
#         l.append(args[i])
#     return max(l)
#
#
# res = func_6(1, 2, 3)
# print(res)

# - створити функцію яка повертає найменьше число з ліста

# def func_7(*args):
#     l = []
#     for i in range(len(args)):
#         l.append(args[i])
#     return min(l)
#
#
# res = func_7(1, 2, 3)
# print(res)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def func_8(*args):
#     l = []
#     for i in range(len(args)):
#         l.append(args[i])
#     l.sort()
#     return l
#
#
# res = func_8(3, 1, 2)
# print(res)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# l = [1, 2, 3, 4, 5, 6]
#
#
# def func_9(list):
#     avg = sum(list) / len(list)
#     return avg
#
#
# res = func_9(l)
# print(res)

# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def decorator(func):
#     def inner():
#         text = func()
#         print(func().replace('_', ' '))
#     return inner
#
#
# @decorator
# def pr():
#     return 'Hello_boss_!!!'
#
#
# pr()
