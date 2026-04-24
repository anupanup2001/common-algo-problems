# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = root.val
        
        def dfs(node):
            if not node:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            
            if right < 0:
                right = 0
            if left < 0:
                left = 0
            self.res = max(self.res, node.val + left + right)
            print(self.res)
            return max(node.val + left, node.val + right)

        dfs(root)
        return self.res
        
        