# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        current_node = root
        if current_node == None:
		    return []
        else:
            part1 = self.inorderTraversal(current_node.left)
            print(type(part1))
            output.append(current_node.val)	#append returns the list in place.
            part3 = self.inorderTraversal(current_node.right)
            print(type(part3))
        
        return part1 + output + part3    

        #if root==None:
        #    return []
        #return self.inorderTraversal(root.left) + [root.val] + self.[root.right]

        
