"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        table = dict()
        visited = set()
        stack = []
        visited.add(node)
        stack.append(node)
        table[node] = Node(node.val,[])

        while stack:
            #remove node from the queue
            currNode = stack.pop()

            for nei in currNode.neighbors:
                if nei not in visited:
                    #add new entry to table
                    newNode = Node(nei.val,[])
                    table[nei] = newNode
                    visited.add(nei)
                    stack.append(nei)
                #assume that currNode is already in the table, since it should already be in the visited set.
                table.get(currNode).neighbors.append(table.get(nei))
                #currnode.neighbors = table[neighbor]


        return table.get(node)
