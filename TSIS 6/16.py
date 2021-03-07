l = []
for x in range(1, 31):
    l.append(x)
print(*(x**2 for x in l))