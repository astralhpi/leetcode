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
        duplicateTable = defaultdict(dict)
        result = []
        for i in xrange(0, len(nums) - 2):
            for j in xrange(i + 1, len(nums) - 1):
                n1 = nums[i]
                n2 = nums[j]
                n3 = - (n1 + n2)
                idxTable[n1] -= 1
                idxTable[n2] -= 1
                if n3 in idxTable and idxTable[n3] != 0:
                    item = sorted([n1, n2, n3])
                    if item[1] not in duplicateTable[item[0]]:
                        result.append(item)
                        duplicateTable[item[0]][item[1]] = True
                idxTable[n1] += 1
                idxTable[n2] += 1
        return result
                                
                            
