# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if self.isLeaf(root):
            return sum == root.val

        result = False
        if root.left is not None:
            result = result or self.hasPathSum(root.left, sum - root.val)
        if root.right is not None:
            result = result or self.hasPathSum(root.right, sum - root.val)
        return result

    def isLeaf(self, node):
        return (node.left, node.right) == (None, None)
        
