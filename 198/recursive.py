class Solution(object):
    def rob(self, nums):
        self.cache = {}
        return self.robIter(nums, 0)


    def robIter(self, nums, curIdx):
        if curIdx in self.cache:
            return self.cache[curIdx]
            
        if len(nums) <= curIdx:
            return 0
            
        result = max(
            nums[curIdx] + self.robIter(nums, curIdx+2),
            self.robIter(nums, curIdx+1))
        
        self.cache[curIdx] = result

        return result
        
        
        
