# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Base Case
        if not p and not q:
            return True
        
        #If not p or q and if the values in either do not match return False
        if not p or not q or p.val != q.val:
            return False
        
        #Recursive call on both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)