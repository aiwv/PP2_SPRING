# v, t = map (int, input().split()) 
v = int(input())
t = int(input())
res = v * t
if res > 0:
    print (res % 109)
else:
    print (109 - (-1)*res % 109))
# print (res % 109) if res > 0 else print (res - (res % 109))