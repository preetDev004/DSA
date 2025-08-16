from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(root):
            if not root:
                return False
            elif k - root.val in seen:
                return True
            seen.add(root.val)
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
            