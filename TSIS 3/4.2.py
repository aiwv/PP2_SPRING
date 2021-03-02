n, m = map(int, input().split())
l = set()
t = set()
for i in range(n):
    x = int(input())
    l.add(x)
for i in range (m):
    x = int(input())
    t.add(x)

print(len(set(l) & set(t)))
print(*sorted(set(l) & set(t), key=int))
print(len(l.difference(t)))
print(*sorted(l.difference(t), key=int))
print(len(t.difference(l)))
print(*sorted(t.difference(l), key=int))