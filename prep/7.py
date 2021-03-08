# find sequences of lowercase letters joined with a underscore.
import re
s = input()
res = re.findall('^[a-z]+_[a-z]+$', s)
print(bool(res))