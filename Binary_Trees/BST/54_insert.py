from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def searchVal(root, val):
            if not root or root.val == val:
                return root
            return searchVal(root.right, val) if val > root.val else searchVal(root.left, val)

        return searchVal(root, val)
    