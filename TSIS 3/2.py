a = list(input().split())
mini = 1000 
for i in range(len(a)):
    x = int(a[i])
    if x > 0 and x < mini:
        mini = x
print(mini)