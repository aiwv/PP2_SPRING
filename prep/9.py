# matches a string that has an 'a' followed by anything, ending in 'b'
import re
s = input()
res = re.findall('[a].*[b]$', s)
print(bool(res))