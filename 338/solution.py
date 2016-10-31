import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num + 1)
        
        offset = 1
        for i in xrange(1, num + 1):
            if offset <= i/2:
                offset *= 2
            result[i] = result[i-offset] + 1
        return result
