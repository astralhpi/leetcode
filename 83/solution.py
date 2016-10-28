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
        cur = head
        while cur != None:
            next = cur.next
            if next is not None and next.val == cur.val:
                cur.next = next.next
            else:
                cur = next
        return head
        
