a = int(input())
b = int(input())
c = int(input())
x1 = (-b - (b**2 - 4 * a * c)**0.5)/(2*a)
x2 = (-b + (b**2 - 4 * a * c)**0.5)/(2*a)
if x1 == x2:
    print(1, int(x1))
elif x1 != x2:
    print(2, int(x1), int(x2))
else:
    print(0) 