class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxTable = {}
        cur_max = 0
        for i in xrange(len(prices)-1, 0, -1):
            cur_max = max(cur_max, prices[i])
            maxTable[i] = cur_max
        
        result = 0
        for idx, price in enumerate(prices[:-1]):
            result = max(maxTable[idx+1] - price, result)
        return result
