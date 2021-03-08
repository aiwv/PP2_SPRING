n = int(input())
l = []
for _ in range(0, n):
    s = input()
    l.append(set(s))
for i in range(0, len(l)-1):
    x = l[i].intersection(l[i+1])
    if x == set():
        print('NO COMMON CHARACTERS')
        break
if x:
    print(*sorted(x))