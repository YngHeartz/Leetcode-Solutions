# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root, leaf):
            #Base Case
            if not root:
                return
            
            #If leaf node append val to leaf array
            if not root.right and not root.left:
                leaf.append(root.val)
            
            #Recursivly call the dfs function on right and left subtree
            dfs(root.right, leaf)
            dfs(root.left, leaf)
        
        
        #Create two empty arrays
        leaf1, leaf2 = [], []

        #Call dfs function on roo1 and root2 and then save vals to each array respectivly
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        #Compare leaf1 array to leaf2 array if same return True else return False
        return leaf1 == leaf2