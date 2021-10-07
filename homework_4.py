# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.area = self.x * self.y
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def len(self):
#         return self.x + self.y
#
#
# rectangle1 = Rectangle(2, 3)
# rectangle2 = Rectangle(4, 5)
#
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 < rectangle2)
# print(rectangle1.len(),rectangle2.len())

# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта, __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

# При створенні об'єкта. Мається на увазі конструктор?

# list = []
#
# class Latter:
#     __count = 0
#
#     def __init__(self):
#         self.__text = None
#         Latter.__count += 1
#
#     @property
#     def text(self):
#         return self.__text
#
#     @text.setter
#     def text(self, new_value):
#         self.__text = new_value
#
#     @classmethod
#     def count(cls):
#         return cls.__count
#
#     def add(self):
#         list.append(self.__text)
#
#
# letter1 = Latter()
#
# letter1.text = 'hi'
# print(letter1.text)
#
# letter1.add()
#
# print(list)

# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.count += 1
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def num(self):
#         return self.count
#
#
# class Prince(Human):
#     def __init__(self, name, age, search):
#         super().__init__(name, age)
#         self.search = search
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def cind_list(self, c_list):
#
#         for i in range(len(c_list)):
#             if c_list[i].size == self.search:
#                 return c_list[i].name
#
#
# c_list = [Cinderella('Alina', '19', 36),
#           Cinderella('Dasha', '20', 37),
#           Cinderella('Masha', '21', 35)]
#
# prince = Prince('Patrik', '25', 35)
#
# print(prince)
#
# print(prince.cind_list(c_list))
#
# print(Cinderella.count)
