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
        #Base case if no node return None
        if not node:
            return None
        
        #Create an empty dict
        nto = {}

        def dfs(node):
            #If node already in dict return the list of nodes
            if node in nto:
                return nto[node]
            
            #Create a copy of the node val and assign it to the nto node
            copy = Node(node.val)
            nto[node] = copy

            #Recursion to create the copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
            
        return dfs(node)