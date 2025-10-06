/*Given a reference of a node in a connected undirected graph.

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
*/

// Working
/*
1: Fill frontier with OLD values and add NEW node to graph with old node as KEY
2: Take top of frontier => create a new node with val and NO neighbors
    b) add top of froniter (old) and new node to graph (unordered_map)
    c) pop frontier
3: repeat 1 until frontier is empty
4: Get element m in OG graph.
    - go through neighbors, get neighbor n
    - neighbor n is a KEY in the NEW_GRAPH
        - go to n's value in NEW_GRAPH and create a ptr to it
        - this ptr is saved in NEW_GRAPH.at(m)->neighbors.push_back(NEW_GRAPH.at(n))
    b) repeat above for every m in the OG graph
5: return a ptr to the new root node
*/

#include "133. Clone Graph.h"

Node* Solution::cloneGraph(Node* root) {
    if (!root) {
        return nullptr;
    }
    Node* nRoot = new Node(root->val);
    
    unordered_map<Node*, Node*> graph;
    queue<Node*> frontier;

    graph.insert({ root, nRoot });
    frontier.push(root);


    while (!frontier.empty()) {
        Node* oldNode = frontier.front();
        frontier.pop();

        Node* newNode = graph.find(oldNode)->second;

        for (Node* neighbor : oldNode->neighbors) {
            if (graph.find(neighbor) == graph.end()) { // old neighbor NOT in graph => put in graph
                frontier.push(neighbor);
                graph.insert({ neighbor, new Node(neighbor->val) });
                // made a node for the neighbor, now make a ptr to its new value   
            }
            // old neighbor IN graph 
            Node* newNeighbor = graph.find(neighbor)->second;
            newNode->neighbors.push_back(newNeighbor);
        }
    }

    return graph.find(root)->second;
} 