import re
res = re.fullmatch("[a-zA-Z0-9_]+", input())
if res:
    print("Found a match!")
else:
    print("Not matched")