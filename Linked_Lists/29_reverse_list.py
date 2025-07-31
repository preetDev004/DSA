from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        prev = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        return prev
        
    def reverseList_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head or not head.next:
            return head

        def reverse_recursive(curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            return reverse_recursive(next, curr)

        return reverse_recursive(head, None)
    
