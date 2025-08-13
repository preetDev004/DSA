from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev_subtree(root):
            if not root: 
                return root
            
            left_subtree = rev_subtree(root.left)
            right_subtree = rev_subtree(root.right)

            root.left, root.right = right_subtree, left_subtree
            return root

        rev_subtree(root)
        return root