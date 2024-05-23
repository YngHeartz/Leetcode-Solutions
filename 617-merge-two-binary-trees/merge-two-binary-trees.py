# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base Case
        if not root1 and not root2:
            return None
        #Base case for root1
        if not root1:
            return root2
        #Base case for root2
        if not root2:
            return root1
        
        #Creates a variable that will store the added values together at the treenode TreeNode will get the current values in each of the nodes
        merged = TreeNode(root1.val + root2.val)
        #recursive call for the right and left subtrees
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged
