# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        #Create empty list
        res = []

        #Helper function
        def findval(root):
            #If not root return
            if not root:
                return
            #Get right and left values and store them into res
            res.append(root.left.val)
            res.append(root.right.val)
        #Call the function on the root
        findval(root)
        #Return the sum of res and check if its equal to the root.val and if it is return True else return False
        return sum(res) == root.val            