# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def recur(A, B):
            if not A and B: # A 找完了还没有找到相同的结点
                return False
            if not A and not B: # A和B都找完了
                return True
            if A == B: # A和B是相同结点，比较其子树是否相同
                return recur(A.left, B.left) and recur(A.right, B.right)
            if not A.left:
                left = recur(A.left, B)
            if not A.right:
                right = recur(A.right, B)
            return left or right
        return recur(A,  B)
A = [3,4,5,1,2]
B = [4,1]
print(Solution().isSubStructure(A,B))