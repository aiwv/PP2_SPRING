l = map(int, input().split())
a = dict()
for i in l:
    if i not in a:
        a[i] = 0
    a[i] += 1
for key in a:
    print(key, end=' ')