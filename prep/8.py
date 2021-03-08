import re
s = input()
res = re.findall('^[A-Z].*[a-z]$', s)
print(bool(res))