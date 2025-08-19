from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balance(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.nodes = []
        self.BSTToArray(root)
        return self.ArrayToBST(0, len(self.nodes) - 1)

    def BSTToArray(self, root):
        if not root:
            return
        self.BSTToArray(root.left)
        self.nodes.append(root)
        self.BSTToArray(root.right)

    def ArrayToBST(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = self.nodes[mid]
        root.left = self.ArrayToBST(start, mid-1)
        root.right = self.ArrayToBST(mid+1, end)
        return root

