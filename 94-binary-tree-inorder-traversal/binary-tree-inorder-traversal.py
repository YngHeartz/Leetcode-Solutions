# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Empty Array
        res = []
        def helper(root):
            #Base Case
            if not root:
                return
            #Recursive Call on the left subtree and right subtree
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        #Call the helper function on the root
        helper(root)
        #Return the res array
        return res            