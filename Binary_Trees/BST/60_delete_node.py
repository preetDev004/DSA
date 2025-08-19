from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity: O(h) - h is the height of the tree
# Space Complexity: O(h) - h is the height of the tree
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        # if key is greater than root.val, delete from right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # if key is less than root.val, delete from left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if key is equal to root.val
        else:
            # no child 
            if not root.left and not root.right:
                return None
            # one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # two children -> find successor and replace root.val with successor.val
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            # delete successor from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        # return updated root
        return root