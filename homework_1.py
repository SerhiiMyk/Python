# 1)Дан лист:
l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - найти min число в листе
# l.sort()
# print(l[0])
# or
# print(min(l))

#   - удалить все дубликаты в листе

# i=0
# while i < len(l):
#     if l.count(l[i])>=2:
#         l.remove(l[i])
#     i += 1
# print(l)

#   - заменить каждое четвертое значение на "Х"

# for i in range (4,len(l),4):
#     l[i]='x'
# print(l)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:


# a=input('input length the side of the square:')
# a=int(a)
#
# for i in range(a):
#     for k in range(a):
#         if i==0 or i==a-1:
#             print('*', end='')
#         elif k==0 or k==a-1:
#             print('*', end='')
#         else :
#             print(' ',end='')
#     print()

# 3) вывести табличку умножения с помощью цикла while

# i = 1
# while i < 10:
#     k = 1
#     while k < 10:
#         print(f'{i * k:2}', end=' ')
#         k += 1
#     print()
#     i += 1

# 4) переделать первое задание под меню с помощью цикла
# i = 1
# while i!=0:
#     print('1.найти min число в листе\n2.удалить все дубликаты в листе\n3.заменить каждое четвертое значение на "Х"\n4.Exit\n')
#     select_item = int(input('select a menu item:'))
#     if select_item==1:
#         print('\nmin number is:',min(l),'\n')
#     elif select_item==2:
#         l.sort()
#         i=0
#         while i < len(l):
#             if l.count(l[i])>=2:
#                 l.remove(l[i])
#             i += 1
#         print('\nnew list:',l,'\n')
#     elif select_item==3:
#         for i in range (4,len(l),4):
#             l[i]='x'
#         print('\nnew list:',l,'\n')
#     elif select_item==4:
#         i=0
#     else:
#         print('\nyou have chosen the wrong item, please try again\n')


# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

l.sort()
i = 0
while i < len(l):
    if l.count(l[i]) >= 2:
        l.remove(l[i])
    i += 1
    newl = l
print('\nlist:', newl)
avg = sum(newl) / len(newl)
print('\naverage is -', avg)

for i in range(0, len(newl)):
    if newl[i] > avg:
        less_index = i - 1
        if (avg - newl[less_index]) < (newl[i] - avg):
            print('\nthe nearest number to average is -', newl[less_index])
            break
        else:
            print('\nthe nearest number to average is -', newl[i])
