import math
s = 0
for i in range(1, 11):
    i = 1 / (i**2)
    s += i
print(math.sqrt(6*s))