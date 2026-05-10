#include "133. Clone Graph.cpp"

int main()
{
    Solution graph;
    Node* node1 = new Node(1);
    Node* node2 = new Node(2);
    Node* node3 = new Node(3);
    Node* node4 = new Node(4);

    node1->neighbors.push_back(node2);
    node1->neighbors.push_back(node4);

    node2->neighbors.push_back(node1);
    node2->neighbors.push_back(node3);

    node3->neighbors.push_back(node2);
    node3->neighbors.push_back(node4);

    node4->neighbors.push_back(node1);
    node4->neighbors.push_back(node3);
    Node* a = graph.checkAnswer(node1);

    for (Node* i : a->neighbors) {
        cout << i->val;
    }
    return 0;
}