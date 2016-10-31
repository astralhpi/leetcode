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
        diff = None
        count = 2
        for i in xrange(1, len(A)):
            if A[i-1] - A[i] == diff:
                count += 1
            else:
                diff = A[i-1] - A[i]
                result.append(count)
                count = 2
        result.append(count)
        return result
