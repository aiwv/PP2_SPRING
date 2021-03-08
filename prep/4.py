import re
s = input()
def check(s):
    res = re.search('ab?', s)
    return bool(res)
print(check(s))