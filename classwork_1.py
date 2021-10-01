
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


notebook = dict()
price_list=[]

j=1
while j!=0:
    print('\n1) Создать запись\n'
          '2) Список все записей\n'
          '3) Общая сумма всех покупок\n'
          '4) Самая дорогая покупка\n'
          '5) Поиск по названию покупки\n'
          '6) Выход')
    select_item = int(input('\nselect a menu item: '))
    if select_item == 1:
        i=1
        while i!=0:
            p_name = input('\nwrite name of the product: ')
            p_price = int(input('write price of the product: '))
            notebook.update({p_name:p_price})
            # print('\n', notebook, '\n')
            i=int(input('if you want to add one more item press 1 or if you want to exit press 0: '))
            if i!=1 and i!=0:
                while i!=1 or i!=0:
                    i = int(input('\nPlease press 1 or 0: '))
                    if i==1 or i==0:
                        break
    elif select_item==2:
        for k,v in notebook.items():
            print('\n',k,' - ',v,'UAH')
            price_list.append(v)
        print()
    elif select_item == 3:
        print('\nThe total amount of all purchases: ', sum(price_list),'UAH')
    elif select_item == 4:
        print('The most expensive purchase: ', max(price_list),'UAH')
    elif select_item == 5:
        search=input('\nenter the product name: ')
        for k,v in notebook.items():
            if search==k:
                print('\nproduct cost: ',v,'UAH')
    elif select_item==6:
        j=0

