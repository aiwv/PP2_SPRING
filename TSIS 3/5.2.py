# Словарь синонимов
n = int(input())
d = {}
for i in range(n):
    x, y = input().split()
    d[x] = y
    d[y] = x
print(d[input()])