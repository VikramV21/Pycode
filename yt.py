n = input('>>>>')
# if n.isinstance():
#     print(True)
# print(isinstance(-5, int))
if n[0]=='-':
    if n[1:].isdigit():
        print('Int')

elif n.isdigit():
    print('Int2')
elif n.isalpha():
    print('Str')
elif '.' in n:
    print('f')
else:
    print("This is something else")
