class Solution(object):
    def hammingDistance(self, x, y):
        k = x ^ y
        result = 0
        while k > 0:
            if k & 1:
                result += 1
            k >>= 1
        return result
