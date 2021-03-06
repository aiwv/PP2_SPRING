import re
for _ in range(int(input())):
   res = input()
   res = re.sub(r"\s\&\&\s"," and ",res)
   res = re.sub(r"\s\|\|\s"," or ",res)
   res = re.sub(r"\s\&\&\s"," and ",res)
   res = re.sub(r"\s\|\|\s"," or ",res)
   print(res)