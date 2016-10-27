class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        return reduce(lambda x, y: self.prefix(x, y), strs)
    
    def prefix(self, left, right):
        minLen = min(len(left), len(right))
        for i in xrange(0, minLen):
            if left[i] != right[i]:
                return left[:i]
        return left[:minLen]
