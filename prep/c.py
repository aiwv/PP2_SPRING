n = int(input())
A = input().split()
S = set(A)

if len(A) == len(S):
    print('YES')
else:
    print('NO')