# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def is_sys_tree(self, root):
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)
















print("--------------------ansert----------------------思路1")


# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#
#         def check(node1, node2):
#             if not node1 and not node2:
#                 return True
#             elif not node1 or not node2:
#                 return False
#
#             if node1.val != node2.val:
#                 return False
#             return check(node1.left, node2.right) and check(node1.right, node2.left)
#
#         return check(root, root)


