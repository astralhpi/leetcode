class Solution(object):
    def rob(self, nums):
        
        cur = 0
        last = 0

        for num in nums:
            tmp = last
            last = cur
            cur = max(tmp + num, cur)
        return cur
