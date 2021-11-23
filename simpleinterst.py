# p = 1000
# t = 2
# r = 4
#
#
# def simple_interst(p, t, r):
#     print("The principle amount is", p)
#     print("The time is", t)
#     print("The rate is", r)
#
#
# Si = (p * t * r) / 100
# op = int(Si)
# print(op)
# class Book:
#     def __init__(self, value):
#         self.__pages = value
#
#     def SetData(self, value):
#         if value >= 1:
#             self.__pages = value
#
#     def getData(self):
#         return self.__pages
#
#
# b = Book(100)
# b.SetData(114)
# num = b.getData()
# print(num)
# b.SetData(-99)
# num = b.getData()
# print(num)

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")




class USA():

    def language(self):
        print("English is the primary language of USA.")

    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def type(self):
        print("USA is a developed country.")


ind = India()
usa = USA()
for country in (ind, usa):
    country.capital()
    country.language()
    country.type()
