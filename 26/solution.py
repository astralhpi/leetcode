class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != nums[i+1]:
                nums[count] = nums[i]
                count += 1
        return count
