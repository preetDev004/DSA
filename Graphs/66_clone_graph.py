from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        clones = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    q.append(neighbor)
                    clones[neighbor] = Node(neighbor.val)
                clones[curr].neighbors.append(clones[neighbor])

        return clones[node]
