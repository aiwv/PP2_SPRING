f = open('t1.txt', "a")
f.write("ddd\nfff")
f.close()
f = open('t1.txt', "r")
data = f.read()
print(data)
f.close()