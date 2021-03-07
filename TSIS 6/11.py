n = int(input())
l = []
for i in range (1, n):
    if n % i == 0:
        l.append(i)
print(bool(sum(x for x in l) == n))