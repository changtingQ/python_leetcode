# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        def cal_depth(p, q):
            if not p and not q:
                return self.depth
            if p and not q:
                self.depth += 1
                return self.cal



















print("--------------------answer------------------思路1")