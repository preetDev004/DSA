from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy_head = ListNode(-1, head)
        left_prev, curr_node = dummy_head, head
        for _ in range(left-1):
            left_prev = curr_node
            curr_node = curr_node.next
            
        prev = None
        for _ in range(right-left+1):
            curr_node.next, prev, curr_node = prev, curr_node, curr_node.next
        
        left_prev.next.next, left_prev.next = curr_node, prev

        return dummy_head.next
