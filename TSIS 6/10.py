l = map(int, input().split())
print(*list(filter(lambda x: x % 2 == 0, l)))