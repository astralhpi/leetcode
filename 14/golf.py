from itertools import takewhile
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return "".join([y[0] for y in takewhile(lambda x: len(set(x))==1, zip(*strs))])
