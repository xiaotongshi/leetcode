# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, level):
            if root is None:
                return level
            level += 1
            l1 = dfs(root.left, level)
            l2 = dfs(root.right, level)
            return max(l1, l2)
            
        return dfs(root, 0)




