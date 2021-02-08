class Solution:
    def largestAltitude(self, gain):
        l = [0]
        for i in range (len(gain)):
            l.append(l[i] + gain[i])
        return max(l)