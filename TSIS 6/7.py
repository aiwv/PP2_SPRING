s = input()
u = 0
l = 0
for x in s:
    if x.isupper():
        u += 1
    elif x.islower():
        l +=1
print ("No. of Upper case characters : ", u)
print ("No. of Lower case characters : ", l)