def prime(num):
    if num == 2:
        return True
    for i in range(2, num+1):
        if num % i == 0:
            return False
        return True
n = int(input())
print(bool(prime(n)))