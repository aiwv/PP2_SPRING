n = int(input())
f = open('t1.txt', "r")
for _ in range(n):
    line = f.readline()
    print(line)