class Solution(object):
    def swapPairs(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head
    
        tail = head.next.next
        newHead = head.next
        newHead.next = head
        head.next = self.swapPairs(tail)
        
        return newHead
