"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # one way = make a dict of node copies
        # then just remake the og using that dict
        # kinda memory intensive, saving all those extra nodes
        # 
        """if not node:
            return None
        nodeDict = {}
        nodeList = [node]
        nodeSet = set([node])
        for curr in nodeList:
            if not nodeDict.get(curr.val):
                currCopy = Node(val = curr.val)
                nodeDict.update({curr.val:currCopy})
            for neighborNode in curr.neighbors:
                if neighborNode.val not in nodeDict and neighborNode.val not in nodeSet:
                    nodeList.append(neighborNode)
                    nodeSet.add(neighborNode.val)

        for curr in nodeList:
            currClone = nodeDict.get(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in currClone.neighbors:
                    cloneNeighbor = nodeDict.get(neighbor.val)
                    currClone.neighbors.append(cloneNeighbor)
            
        return nodeDict.get(1)"""

        # O(N^2), so not very good, but its a solution.

        # Better solution = do both at the same time
        # So bredth first search = add neighbors to nodeList
        # If an element is in the graph already, just skip it
        # So in one pass it has to
        # get curr element
        # check if its been seen already
        # create clone and copy val over
        # for neighbor in old.neighbors:
        #   if neighbor in nodeDict:
        #       curr.add(neighbor)
        #       neighbor.add(curr)
        # this way its adding both ways the moment its node is created
        # So how can I not read nodes that are in the list but not dict, into the list
        # either the nodeSet to keep track or just let it loop over
        if not node:
            return None
        newNode = Node(val=1)
        nodeDict = {1:newNode}
        nodeList = [node]
        """for curr in nodeList:
            if curr.val not in nodeDict:
                currCopy = Node(val=curr.val)
                nodeDict[curr.val] = currCopy
                for neighbor in curr.neighbors:
                    if neighbor.val in nodeDict:
                       currCopy.neighbors.append(nodeDict.get(neighbor.val))
                       nodeDict.get(neighbor.val).neighbors.append(currCopy)
                    else:
                        nodeList.append(neighbor)
        return nodeDict.get(1)"""
        # code was good but a few things:
        # use a while loop and pop the front element off each time (or back, makes no difference)
        # also, clone on discovery this time
        # don't have to add it to nodeDict on creation, just ADD IT TO nodeList!
        while nodeList:
            curr = nodeList.pop()
            for neighbor in curr.neighbors:
                if neighbor.val not in nodeDict:
                    neighborClone = Node(val=neighbor.val)
                    nodeDict[neighbor.val] = neighborClone
                    nodeList.append(neighbor)
                else:
                    neighborClone = nodeDict.get(neighbor.val)
                nodeDict[curr.val].neighbors.append(neighborClone)
                    
        return nodeDict.get(1)
