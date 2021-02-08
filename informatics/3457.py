a = int(input())
nex = a + 1
prev = a - 1
res = '''The next number for the number {0} is {1}.
The previous number for the number {2} is {3}.'''
print (res.format(a, nex, a, prev))