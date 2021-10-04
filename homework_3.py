# 1.написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все

# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append(todo)
#         return todo_list
#
#     def get_all():
#         nonlocal todo_list
#         print(todo_list)
#
#     return add_todo
#
#
# what_todo = notebook()
#
# what_todo('brash teeth')
# what_todo('do morning exercise')
# what_todo('read the book')
# what_todo('make a breakfast')
# print(what_todo('drive the children to kindergarten'))


# 2) протипизировать первое задание


# def notebook():
#     todo_list = []
#
#     def add_todo(todo: str) -> list[str]:
#         nonlocal todo_list
#         todo_list.append(todo)
#         return todo_list
#
#     def get_all():
#         nonlocal todo_list
#         print(todo_list)
#
#     return add_todo
#
#
# what_todo = notebook()
#
# what_todo('brash teeth')
# what_todo('do morning exercise')
# what_todo('read the book')
# what_todo('make a breakfast')
# print(what_todo('drive the children to kindergarten'))


# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.

# l = [15, 20, 25, 30, 35, 40, 45, 50]
# #
# m = list(map(lambda x: x % 15, l))
#
# for i in range(len(m)):
#     if m[i] == 0:
#         print(l[i])

# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# Пример:
# summ(7) -> 7+77+777=861

# n = int(input('wright the number: '))
#
#
# def sum(n):
#     return n * 1 + n * 11 + n * 111
#
#
# res = sum(n)
# print(res)
