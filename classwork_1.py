
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

j=1
while j!=0:
    print('1) Создать запись\n'
          '2) Список все записей\n'
          '3) Общая сумма всех покупок\n'
          '4) Самая дорогая покупка\n'
          '5) Поиск по названию покупки\n'
          '6) Выход\n')
    select_item = int(input('\nselect a menu item:'))

    notebook = dict()
    if select_item == 1:
        i=1
        while i!=0:
            p_name = input('\nwrite name of the product:')
            p_price = int(input('write price of the product:'))
            notebook.update({p_name:p_price})
            print('\n', notebook, '\n')
            i=int(input('if you want to add one more item press 1 or if you want to exit press 0:'))

    elif select_item==2:

        for k,v in notebook.items():
            print(k,v,sep='-')

    elif select_item==6:
        j=0

