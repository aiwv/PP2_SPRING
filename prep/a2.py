import re
res = re.search("[A-Z][a-z]{2, }", input())
if res:
    print('Found a match!')
else:
    print('Not matched!')