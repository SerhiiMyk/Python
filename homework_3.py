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
#
#     def get_all():
#         nonlocal todo_list
#         return todo_list
#
#     return {
#         "add_todo": add_todo,
#         "get_all": get_all
#     }
#
#
# what_todo = notebook()
# add_todo = what_todo.get('add_todo')('brash teath')
# add_todo = what_todo.get('add_todo')('do morning exercise')
# add_todo = what_todo.get('add_todo')('read the book')
# add_todo = what_todo.get('add_todo')('make a breakfast')
# add_todo = what_todo.get('add_todo')('drive the children to kindergarten')
#
# get_all = what_todo.get('get_all')()
# print(get_all)

# from typing import Callable, Union


# 2) протипизировать первое задание
# Value = Union[Callable[[], list[str]], Callable[[str], None]]
#
#
# def notebook() -> dict[str, Value]:
#     todo_list = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return {
#         "add_todo": add_todo,
#         "get_all": get_all
#     }
#
#
# what_todo = notebook()
# add_todo = what_todo.get('add_todo')('brash teath')
# add_todo = what_todo.get('add_todo')('do morning exercise')
# add_todo = what_todo.get('add_todo')('read the book')
# add_todo = what_todo.get('add_todo')('make a breakfast')
# add_todo = what_todo.get('add_todo')('drive the children to kindergarten')
#
# get_all = what_todo.get('get_all')()
# print(get_all)

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
