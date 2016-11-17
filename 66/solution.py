class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        remains = 1
        for num in reversed(digits):
            num += remains
            remains = num / 10
            num = num % 10
            result.insert(0, num)

        if remains > 0:
            result.insert(0, remains)
        return result
