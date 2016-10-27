class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        cur = 1
        for i in xrange(0, n-1):
            tmp = cur
            cur = prev + cur
            prev = tmp
        return cur
