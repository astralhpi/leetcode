class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        center = len(nums) / 2
        diff = nums[center] - target
        if diff == 0:
            return center
        elif diff > 0:
            return self.searchInsert(nums[:center], target)
        else:
            return center + 1 + self.searchInsert(nums[center+1:], target)
