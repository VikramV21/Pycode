# a = 999
#
#
# def fun1():
#     global a
#     a = 888
#     b = 777
#     print(a)
#     print(b)
#
#
# def fun2():
#     global a
#     a = 666
#     c = 555
#     print(a)
#     print(c)
#
#
# fun1()
# fun2()
# print(a)
#
#
# def fun1():
#     print("Inside Fun1")
#
#
# def fun2(x, y):
#     z = x + y
#     print(z)
#
#
# def display(ptr1, ptr2):
#     ptr1()
#     x = 50
#     y = 40
#     ptr2(x, y)
##
# fun1()
# a = 10
# b = 20
# fun2(a, b)
# ref1 = fun1
# ref2 = fun2
#
# display(ref1, ref2)
# num = 0

#
# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# L = []
# i = 0
# while i <= 4:
#     print("Enter an element")
#     num = int(input())
#     L.insert(i, num)
#     i = i + 1
#
# K = list(filter(even, L))
# print(K)

a = 1000000000000000000
print("a =", a) #Printing the value stored in 'a' variable
print(type(a)) #To find the data type
