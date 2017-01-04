class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            n = nums[i]
            k = nums[n-1]
            if k == n or n == i + 1:
                i += 1
                continue
            nums[n-1] = n
            nums[i] = k
        
        result = []
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                result.append(i+1)
        return result
            
        
