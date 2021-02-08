s = 0
for i in range(1, 11):
    i = (-1)**(i+1) * 4/(2*i - 1)
    s += i
print(s)