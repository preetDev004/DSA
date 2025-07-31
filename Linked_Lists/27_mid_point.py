from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        start = head
        while start.next != None:
            start = start.next
            count += 1

        target = count//2 + 1 
        i = 1
        elem = head
        while i != target and elem.next != None:
            elem = elem.next
            i += 1

        return elem  

    def middle_node_v2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if we have two pointer one go normal speed one go twice as speed so when the fast pointer reaches end the slow one would be at the middle!
        slow = fast = head
        while fast:
            fast = fast.next.next
            slow = slow.next
        return slow
        
        