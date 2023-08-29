# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0

        self.height(root)

        return self.max_diameter 

    
    def height(self, root):
        if not root:
            return -1
        left = self.height(root.left)
        right = self.height(root.right)
        diameter = 2 + left + right
        self.max_diameter = max(self.max_diameter, diameter)
        return 1 + max(left, right)