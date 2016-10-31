class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return sum(map(self.count, map(len, self.slices(A))))
    
    def count(self, length):
        if length < 3:
            return 0
        return (length - 2) * (length - 1) /2

    def slices(self, A):
        result = []
        nums = []
        for num in A:
            if len(nums) < 2:
                nums.append(num)
            elif (nums[-1] - nums[-2]) == (num - nums[-1]):
                nums.append(num)
            else:
                result.append(nums)
                nums = [nums[-1], num]
        result.append(nums)
        return result
                
        
            
