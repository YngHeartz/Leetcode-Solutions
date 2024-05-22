# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Create empty list
        res = []

        #Helper function
        def helper(root):
            #Base Case
            if not root:
                return
            #Checks the left most node and then the children associated and then apends the value to the res and then checks the right side of the node also recursive step since we are calling itself inside the function until all values are read in
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        #calls the calls the helper function on the root
        helper(root)
        #Returns the res list with all the appended numbers
        return res