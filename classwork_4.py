# сделать с файла users.txt
# файл users.json
# который будет хранить json
# в виде:
#
# [{"name":"Ostap","age":16,"gender:"male"},{"name":"Oleg","age":16,"gender:"male"}, ....]
#
# одним словом распарсить файл и сделать json файл
import json

users_list = []

with open('users.txt') as file:
    read = file.readlines()
    for i in read:
        name, age, gender = i.strip().split('|')
        user_d = {'name': name, 'age': int(age), 'gender': gender}
        users_list.append(user_d)
with open('users.json', 'w') as file:
    json.dump(users_list, file)
