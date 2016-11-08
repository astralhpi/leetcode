# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        return self.removeNth(head, self.count(head) - n)
    
    def removeNth(self, head, n):
        if n == 0:
            return head.next
        else:
            head.next = self.removeNth(head.next, n-1)
            return head
    
    def count(self, node):
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count
        
