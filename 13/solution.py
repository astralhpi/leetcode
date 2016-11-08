class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev = 0
        for num in reversed(map(self.signToInt, s)):
            if prev > num:
                result -= num
            else:
                result += num
            prev = num
        return result
            

    def signToInt(self, s):
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        elif s == 'M':
            return 1000
