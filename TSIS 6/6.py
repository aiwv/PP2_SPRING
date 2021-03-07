l = map(int, input().split())
def check(num):
    if num in l:
        return True
    return False
n = int(input())
print(bool(check(n)))