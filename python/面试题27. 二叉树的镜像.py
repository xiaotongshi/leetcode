# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: #p 判断节点是否为空
            return None
        if not root.left and not root.right: # 判断是否是叶节点
            return root
            
        root.left, root.right = root.right, root.left # 交换非叶节点的两个子节点
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        return root