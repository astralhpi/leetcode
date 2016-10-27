class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num != 0:
            if num == 1:
                return True
            num = self.divide(num)
        return False
    
    def divide(self, num):
        for i in [2, 3, 5]:
            if num % i == 0:
                return num / i
        return 0
