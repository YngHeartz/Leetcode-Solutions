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
            return
        
        #If leaf node compare val to targetSum
        if not root.right and not root.left:
            return targetSum == root.val

        #Decrement step        
        targetSum -= root.val

        #Recursive step to check left and right subtrees
        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)