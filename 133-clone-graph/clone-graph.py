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
        if not node:
            return None

        xyz = {}

        def dfs(node):
            if node in xyz:
                return xyz[node]           

            copy = Node(node.val)
            xyz[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)