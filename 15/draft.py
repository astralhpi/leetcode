from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        duplicateTable = defaultdict(dict)
        idxTable = defaultdict(list)
        
        for idx, num in enumerate(nums):
            idxTable[num].append(idx)
        
        result = []
        for i in xrange(0, len(nums) - 2):
            for j in xrange(i + 1, len(nums) - 1):
                r = - (nums[i] + nums[j])
                if r in idxTable:
                    for k in idxTable[r]:
                        if j < k:
                            item = sorted([nums[i], nums[j], r])
                            if item[1] not in duplicateTable[item[0]]:
                                result.append(item)
                                duplicateTable[item[0]][item[1]] = True
        return result
                                
                            
