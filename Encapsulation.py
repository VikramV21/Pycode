# class Student:
#     def __init__(self):
#         self.__name = " "
#
#     def getter(self):
#         return self.__name
#
#     def setter(self, value):
#         self.__name = value
#
#     getset = property(getter, setter)
#
#
# S = Student
# S.getset = "Rakesh"
# msg = S.getset
# print(msg)

class Animal:
    def eat(self):
        print("Amimal is eating")

    def sleep(self):
        print("Animal is Sleeping")

    def breathe(self):
        print("Animal is breathing")


class Tiger(Animal):
    def eat(self):
        print("Tiger is eating")

    def sleep(self):
        print("Tiger is Sleeping")

    def breathe(self):
        print("Tiger is breathing")


class Deer(Animal):
    def eat(self):
        print("Deer is eating")

    def sleep(self):
        print("Deer is Sleeping")

    def breathe(self):
        print("Deer is breathing")


class Monkey(Animal):
    def eat(self):
        print("Monkey is eating")

    def sleep(self):
        print("Monkey is Sleeping")

    def breathe(self):
        print("Monkey is breathing")


t = Tiger()
d = Deer()
m = Monkey()


def allowAnimal(ref):
    ref.eat()
    ref.sleep()
    ref.breathe()


allowAnimal(t)
allowAnimal(d)
allowAnimal(m)
