# 1.сделать функцию которая будет возвращать сумму разрядов числа в виде строки
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


# def func(num):
#     num = str(num)
#     num_len = len(num) - 1
#     res = []
#     for i in num:
#         if i != '0':
#             tmp = i + '0' * num_len
#             res.append(tmp)
#         num_len -= 1
#
#     return '+'.join(res)
#
#
# res = func(70304)
# print(res)

# 2.создать функцию которая будет выводить сколько и каких символов в строке
# пример:
# st = 'as 23 fdfdg544
#
# 'a' -> 1
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
#
st = 'as 23 fdfdg544'


def count(sting):
    st_list = list(st)
    clean_list = list(st)

    for i in clean_list:
        if clean_list.count(i) >= 2:
            clean_list.remove(i)

    for i in clean_list:
        num = (st_list.count(i))
        print(i, '->', num)


count(st)
