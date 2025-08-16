
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

        
    def lowestCommonAncestor_v2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':            
        if root == None or root == p or root == q: return root

        left = right = None
        if p.val > root.val and q.val > root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            left = self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
    
        return left or right