# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if leftDepth > rightDepth:
            return leftDepth + 1
        else: 
            return rightDepth + 1

        # Algorithmically this is perfect in terms of time complexity
        # Memory space is large though, for massive binary trees will crash
        # need a non-recursive implementation

    def maxDepthOptimized(self, root):
        if not root:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            currLevel = len(queue)

            for i in range(currLevel):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
