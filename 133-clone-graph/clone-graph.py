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
        # Base case: if the input node is None, return None
        if not node:
            return None
        
        # Create an empty dictionary to map original nodes to their copies
        nto = {}

        def dfs(node):
            # If the node has already been copied, return the copy from the dictionary
            if node in nto:
                return nto[node]
            
            # Create a copy of the current node and add it to the dictionary
            copy = Node(node.val)
            nto[node] = copy

            # Recursively copy all the neighbors of the current node
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            # Return the copy of the current node
            return copy

        # Initiate DFS to clone the entire graph starting from the input node
        return dfs(node)