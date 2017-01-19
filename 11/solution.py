class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        result = 0
        while i != j:
            if height[i] > height[j]:
                size = (j-i) * height[j]
                j -= 1
            else:
                size = (j-i) * height[i]
                i += 1
            result = max(result, size)
        return result
                
                
        
