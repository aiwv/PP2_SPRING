n, h = map(int, input().split())
for _ in range(0, n):
    x, y, z = map(int, input().split())
    ave = (x+y+z)/3
if ave >= h:
    print('YES')
else:
    print('NO')