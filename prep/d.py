seq = input()
X, Y = map(int, input().split())
x, y = 0, 0
lx = []
ly = []
for i in range(len(seq)):
    if seq[i] == "R":
        x, y = x+1, y
        lx.append(x)
        ly.append(y)
    elif seq[i] == "L":
        x, y = x-1, y
        lx.append(x)
        ly.append(y)
    elif seq[i] == "U":
        x, y = x, y+1
        lx.append(x)
        ly.append(y)
    elif seq[i] == "D":
        x, y = x, y-1
        lx.append(x)
        ly.append(y)
ok = False
for i in range (len(lx)):
    if X == lx[i] and Y == ly[i]:
        ok = True
if ok == True:
  print("Passed")
else:
  print("Missed")