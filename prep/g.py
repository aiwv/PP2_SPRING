import re
txt = input()
t = input()
s = input()
f = input()
res1 = re.sub(t, s, txt)
res2 = re.findall(f, res1)
print(len(res2))