# rows = 5
# num = 0
# for i in range(rows, 0, -1):
#
#     num += 1
#
#     for j in range(1, i + 1):
#         print(num, end=' ')
#     print('\r')
#
#
# rows = 5
# for row in range(1, rows + 1):
#
#     for column in range(1, row + 1):
#         print(column, end=" ")
#
#     print(" ")

n = int(input())
i = 6

while 0<i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i - 1