list1 = input().split()
list2 = []
list3 = []
for x in list1:
    if x != '0':
        list2.append(x)
    else:
        list3.append(x)
list2.extend(list3)
print(*list2)