class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = min(nums)
        return sum(map(lambda x: x - minNum, nums))
