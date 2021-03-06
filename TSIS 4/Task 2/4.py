S = input()
k = input()
import re
pattern = re.compile(k)
res = pattern.search(S)
if res:
    while res:
        print("({0}, {1})".format(res.start(), res.end()-1))
        res = pattern.search(S, res.start()+1)
else:
    print("(-1, -1)")