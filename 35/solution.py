class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums)
        
        while start < end:
            center = (start + end) / 2
            diff = nums[center] - target
            if diff == 0:
                return center
            elif 0 > diff:
                start = center + 1
            else:
                end = center
        
        return start
