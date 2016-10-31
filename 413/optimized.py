class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return sum(map(self.count, self.sliceLengths(A)))
    
    def count(self, length):
        if length < 3:
            return 0
        return (length - 2) * (length - 1) /2

    def sliceLengths(self, A):
        if len(A) < 3:
            return []

        result = []
        prev, cur = A[:2]
        count = 2
        for num in A[2:]:
            if cur - prev == num - cur:
                count += 1
            else:
                result.append(count)
                count = 2
            prev, cur = cur, num
        result.append(count)
        return result
