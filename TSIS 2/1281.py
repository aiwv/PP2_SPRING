class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        a = str(n)
        for i in range (len(a)):
            s += int(a[i])
            p *= int(a[i])
        return p - s