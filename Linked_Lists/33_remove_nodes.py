from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next 

        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list
        curr = self.reverse(head) 
        
        prev = curr
        while prev and prev.next:
            if prev.next.val < prev.val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        # Reverse back to get the final result
        return self.reverse(curr)
            

