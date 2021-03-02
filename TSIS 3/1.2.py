l = list(input().split())
t = []
l.sort()
for i in range (0, len(l) - 1):
    if l[i] != l[i+1]:
        t.append(l[i])
print(len(t) + 1)