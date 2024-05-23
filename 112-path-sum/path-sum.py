# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #Base Case
        if not root:
            return 0
        
        #checks for leaf node and then checks if leaf node is equal to the targetSum value
        if not root.right and not root.left:
            return targetSum == root.val
        
        #Subtraction method
        targetSum -= root.val

        #Recursive call for the right and left subtree
        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)