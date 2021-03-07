import re

n = int(input())
s = input()
m = int(input())
t = input()

s1 = s.split()
res1 = re.findall(s1, t)
if res1 == False:
    print('Missed students: ')
    print('- ', s1)
    
t1 = t.split()
res2 = re.findall(t1, s)
if res2:
    print('Not in the group: ')
        print('- ', t1)



# for _ in s:
#     s1 = s.split()
#     if s1 not in t:
#         print('Missed students: ')
#         print('- ', s1)
# for _ in t:
#     t1 = t.split()
#     if t1 not in s:
#         print('Not in the group: ')
#         print('- ', t1)