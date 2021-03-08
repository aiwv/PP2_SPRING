import re
s = input()
def check(s):
    res = re.fullmatch('[a-zA-Z0-9]+', s)
    return bool(res)
    # res = re.search('[^a-zA-Z0-9]', s)
    # return not bool(res)
print(check(s))