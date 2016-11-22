class Solution(object):
    def cmpPeople(self, left, right):
        if left[0] != right[0]:
            return right[0] - left[0]
        else:
            return left[1] - right[1]
        
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, self.cmpPeople)
        result = []
        for h, k in people:
            result.insert(k, [h, k])
        
        return result
