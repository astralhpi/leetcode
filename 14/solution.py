class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            prefix = self.prefix(prefix, s)
        return prefix
        
    
    def prefix(self, left, right):
        long, short = (left, right) if len(left) > len(right) else (right, left)
        for i in xrange(0, len(short)):
            if short[i] != long[i]:
                return short[:i]
        return short
        
