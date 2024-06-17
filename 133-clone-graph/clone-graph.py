"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Base Case if not node
        if not node:
            return None
        
        #Creates an empty dictonary
        otn = {}


        #Function definition the the paramater of node
        def dfs(node):
            #If the node is in otn list we will return the node from the otn list
            if node in otn:
                return otn[node]
            
            #Create a variable that will store the node value inside of copy and then assign the node in otn to the node value of copy
            copy = Node(node.val)
            otn[node] = copy

            #Loop through the node neighbors left and right to then create the copy of the copy and then return copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        #Recursive method for all the nodes in the graph
        return dfs(node)