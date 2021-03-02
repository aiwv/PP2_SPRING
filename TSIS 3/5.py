# большой сдвиг
l = input().split()
n = int(input())
n %= len(l)
for x in l[-n:] + l[:-n]:
    print(x, end= ' ')