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
            
            #If leaf is found append val to leaf
            if not root.right and not root.left:
                leaf.append(root.val)
            
            #dfs function for the right and left getting all leafs appended to the leaf array
            dfs(root.right, leaf)
            dfs(root.left, leaf)

        #Creates empty arrays that will store the appened values
        leaf1, leaf2 = [], []

        #Recursive call for the root1 and root2
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        #Comparison between leaf1 array and leaf2 array
        return leaf1 == leaf2