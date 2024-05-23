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
            
            #If leaf node append to leaf array
            if not root.right and not root.left:
                leaf.append(root.val)
                return

            #Recursive step to get all leaf's
            dfs(root.right, leaf)
            dfs(root.left, leaf)

                
        #Create empty arrays
        leaf1, leaf2 = [], []
        
        #Call dfs function on the root1 and root2 trees
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        #Comparison between two arrays
        return leaf1 == leaf2