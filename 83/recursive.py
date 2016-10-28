# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        next = head.next
        if next is not None and next.val == head.val:
            return self.deleteDuplicates(next)
        head.next = self.deleteDuplicates(next)
        return head
