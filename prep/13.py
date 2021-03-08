# matches a word containing 'z', not at the start or end of the word.
import re
s = input()
res = re.fullmatch('^[z].+[z]+.+^[z]', s)
print(bool(res))