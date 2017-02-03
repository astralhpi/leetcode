class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.stringify(self.parse(a) + self.parse(b))
    
    def parse(self, binary):
        r = 0
        for n in binary:
            r <<= 1
            r += ord(n) - ord('0')
        return r
    
    def stringify(self, n):
        if n == 0:
            return "0"
        r = ""
        while n > 0:
            r = str(n & 1) + r
            n >>= 1
        return r
