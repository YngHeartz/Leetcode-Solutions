# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Create empty array
        res = []

        #Define a helper function
        def helper(root):
            #Base case
            if not root:
                return

            #append the left most root
            helper(root.left)
            res.append(root.val)
            helper(root.right)
            
        #Recursive call onto the root
        helper(root)
        
        #Return the res array
        return res