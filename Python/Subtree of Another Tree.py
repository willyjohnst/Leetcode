"""Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot 
and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
    def isSameTree(self, nodeA, nodeB):
        if not nodeA and not nodeB:
            return True
        if not nodeA or not nodeB:
            return False
        if nodeA.val != nodeB.val:
            return False
            
        return self.isSameTree(nodeA.left, nodeB.left) and self.isSameTree(nodeA.right, nodeB.right)
