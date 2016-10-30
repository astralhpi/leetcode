from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        countTable = defaultdict(int)
        for num in nums1:
            countTable[num] += 1
        
        result = []
        for num in nums2:
            if num in countTable and countTable[num] > 0:
                result.append(num)
                countTable[num] -= 1
        return result
