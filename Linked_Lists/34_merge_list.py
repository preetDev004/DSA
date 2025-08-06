from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        l1_curr, l1_next = list1, list1.next
        l2_curr, l2_next = list2, list2.next

        if l1_curr.val <= l2_curr.val:
            l1_curr.next = self.mergeTwoLists(l1_next, l2_curr)
            return l1_curr
        else:
            l2_curr.next = self.mergeTwoLists(l2_next, l1_curr)
            return l2_curr

    def mergeTwoList_v2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next, curr, list1 = list1, list1, list1.next
            else:
                curr.next, curr, list2 = list2, list2, list2.next

        if list1 or list2:
            curr.next = list1 if list1 else list2

        return dummy_node.next
