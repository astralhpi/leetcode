from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # 인덱스 테이블을 만들어 줌.
        idxTable = defaultdict(int)
        
        for num in nums:
            idxTable[num] += 1
        
        # 중복 확인 하며 리스트를 만들어 줌.
        result = set()
        for i in xrange(0, len(nums) - 2):
            for j in xrange(i + 1, len(nums) - 1):
                n1 = nums[i]
                n2 = nums[j]
                n3 = - (n1 + n2)
                idxTable[n1] -= 1
                idxTable[n2] -= 1
                if n3 in idxTable and idxTable[n3] != 0:
                    result.add(tuple(sorted([n1, n2, n3])))
                idxTable[n1] += 1
                idxTable[n2] += 1
        return map(lambda x: list(x), result)
                                
                            
