f = open("t1.txt","r")
lines = f.readlines()
n=int(input())
last = lines[-n:]
print(*last, sep='\n')