class Solution:
    def numIdenticalPairs(self, nums):
        a = dict()
        for i in nums:
            if i not in a:
                a[i] = 0
            a[i] += 1
        s = 0
        for values in a:
            s += (values * (values - 1)) // 2
        return s