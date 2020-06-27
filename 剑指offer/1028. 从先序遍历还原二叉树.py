# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        s = S.split('-')

S = "1-2--3--4-5--6--7"
print(Solution().recoverFromPreorder(S))