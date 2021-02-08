a = int(input())
b = int(input())
c = int(input())
arr = []
for i in range (1):
    arr.append(a)
    arr.append(b)
    arr.append(c)
arr.sort()
print (*arr, end=" ")
# if a > b:
#     (a, b) = (b, a)
#     if b > c:
#         (b, c) = (c, b)
# print (a, b, c, end=" ")
