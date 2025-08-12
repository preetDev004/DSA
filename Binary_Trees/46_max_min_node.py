from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxVal = max(root.val, max(self.maxValue(root.left), self.maxValue(root.right)))
        return maxVal

    def minValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        minVal = min(root.val, min(self.maxValue(root.left), self.maxValue(root.right)))
        return minVal

# Main execution
if __name__ == "__main__":
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxValue(root))
    print(sol.minValue(root))


