n = int(input())
l = list(map(int,input().split()))
if (l == sorted(l)):
    print('interesting')
else:
    print('not interesting')