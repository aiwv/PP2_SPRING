# remove leading zeros from an IP address.
import re
s = input()
res = re.sub('\.[0]+', '.', s)
print(res)