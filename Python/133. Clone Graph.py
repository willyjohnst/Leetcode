"""Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). 
For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. 
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newNode = Node(node.val)
        graph = {node:newNode}
        frontier = [node] 
        while len(frontier) != 0:
            currNode = frontier[-1]
            frontier.pop()

            for neighbor in currNode.neighbors:
                if graph.get(neighbor) == None: # neighbor not in graph
                    newNeighbor = Node
                    graph.update( { neighbor : newNeighbor(neighbor.val) } )
                    currNeighbor = graph.get(neighbor)
                    currNode.neighbors.append(currNeighbor)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.extend([node2, node4])
node2.neighbors.extend([node1, node3])
node3.neighbors.extend([node2, node4])
node4.neighbors.extend([node1, node3])

Solution.cloneGraph(Solution, node1)
