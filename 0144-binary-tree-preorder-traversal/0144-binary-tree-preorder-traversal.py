# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            part1 = [root.val]
            part2 = self.preorderTraversal(root.left)
            part3 = self.preorderTraversal(root.right)
            return part1 + part2 + part3
