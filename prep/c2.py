n = input()
a = map(int, input().split())
s = set(a)
l = list(s)
for x, y in zip(range(1, len(s)+1), l):
    print(x, y)