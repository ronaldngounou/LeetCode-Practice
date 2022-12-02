# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None: #Both end nodes are the same
            return True
        elif p == None or q == None: #Both end nodes are not the same
            return False
        elif p.val == q.val:  #checking the nodes
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        
        