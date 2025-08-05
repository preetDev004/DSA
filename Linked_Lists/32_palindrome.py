from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # O(n) time with O(1) space
        # find the middle of the list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # two-pointers 
        left = head
        while prev != None:
            if left.val != prev.val:
                return False
            
            prev = prev.next
            left = left.next
        
        return True

    def isPalindrome_v2(self, head: Optional[ListNode]) -> bool:   # O(n) time with O(n) space
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
        

        

