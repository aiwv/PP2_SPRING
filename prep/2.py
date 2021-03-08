# Write a Python program that matches a string that has an a followed by zero or more b's.
import re
s = input()
def check(s):
    res = re.search('ab*', s)
    return bool(res)
print(check(s))