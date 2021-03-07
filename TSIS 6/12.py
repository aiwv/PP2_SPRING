s = input()
def pal(s):
    for i, j in zip(s, reversed(s)):
        if i == j:
            return True
        return False
print(bool(pal(s)))