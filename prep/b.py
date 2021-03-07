import re
txt = input()
word = input()
pattern = re.compile(word)
res = pattern.search(txt)
if res:
    print("First time ", word, "occured in position: ", res.start())
else:
    print("Not found")