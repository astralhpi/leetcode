class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        big = float(x)
        small = float(0)
        for i in xrange(70):
            center = (big + small) / 2.0
            square = center * center
            if x < square:
                big = center
            else:
                small = center
        return int(center)
                
                
                
                
