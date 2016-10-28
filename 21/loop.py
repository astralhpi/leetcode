# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        cur = None
        while (None, None) != (l1, l2):
            if l1 is None:
                next = l2
                l2 = None
            elif l2 is None:
                next = l1
                l1 = None
            elif l1.val < l2.val:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next
            if cur is None:
                head = next
            else:
                cur.next = next
            cur = next
        return head
            
