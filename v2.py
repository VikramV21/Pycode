print("enter the value of a")
a = int(input())
print("enter the value of b")
b = int(input())
print("enter the value of c")
c = int(input())
if a > b:
    if a > c:
        print("A is greatest")
    else:
        print("C is Greatest")
else:
    if b > c:
        print("B is greatest")
    else:
        print("C is greatest")
print("program ends")
