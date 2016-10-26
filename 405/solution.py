class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = 0xffffffff + 1 + num
            
        result = ""
        while True:
            result += self.toHexDigit(num & 0xf)
            num = num >> 4
            if num <= 0:
                break
        
        return result[::-1]
    
    def toHexDigit(self, digit):
        if digit < 10:
            return str(digit)
        else:
            return chr(digit + ord('a') - 10)
            
        
        
