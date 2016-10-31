class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while (result+1)*(result+2) <= 2*n:
            result += 1
        return result
        
