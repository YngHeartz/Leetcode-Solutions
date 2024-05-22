# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        #Helper function for recursion
        def helper(root, leaf):
            #If node is empty return
            if not root:
                return
            #If we reach a leaf node append it to the leaf array
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            #Recursive step for the left subtree and leafs and for the right subtree with its leafs
            helper(root.left, leaf)
            helper(root.right, leaf)

        #Creates empty arrays
        leaf1, leaf2 = [], []

        #Calls the helper function with the params of roo1 and and appends all leaves to the leaf 1 and then does the same but for root2 and leaf2
        helper(root1, leaf1)
        helper(root2, leaf2)

        #Returns the comparison of the two arrays
        return leaf1 == leaf2
            
