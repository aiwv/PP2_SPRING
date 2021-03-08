# matches a word at the beginning of a string
import re
s = input()
def check(s):
    res = re.search('^\w+', s)
    return bool(res)
print(check(s))