class Solution(object):
    def __init__(self):
        self.cacheTable = {
            -1:0,
            0:1
        }
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cacheTable:
            return self.cacheTable[n]
        
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cacheTable[n] = result
        return result
        
