# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        curr = head
        next_node = head.next
        prev = None

        while next_node:
            if next_node.val:
                curr.val += next_node.val
            else:
                curr.next = next_node
                prev = curr
                curr = curr.next
            next_node = next_node.next
        
        prev.next = None

        return head

        # curr = head
        # next_node = head.next
        # total = 0

        # while next_node:
        #     if next_node.val:
        #         total += next_node.val
        #     else:
        #         curr = curr.next
        #         curr.val = total
        #         total = 0
        #     next_node = next_node.next

        # curr.next = None
        # return head.next
        