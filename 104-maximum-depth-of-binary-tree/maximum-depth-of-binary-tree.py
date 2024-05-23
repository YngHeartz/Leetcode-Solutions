# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Base Case
        if not root:
            return 0
        
        #Return the max depth between the right and left subtrees
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))