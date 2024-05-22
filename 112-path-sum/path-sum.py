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
            return False
        
        #if we reach a leaf node check to see if the value in leaf node is equal to the target sum
        if not root.right and not root.left:
            return root.val == targetSum
        
        #Decrement the target sum by the current value in the current node
        targetSum -= root.val

        #Recursive step to check the left and right side of the tree
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)