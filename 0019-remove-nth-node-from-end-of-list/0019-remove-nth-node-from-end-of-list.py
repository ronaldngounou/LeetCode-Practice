# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # To solve this, first I count all the elements. 
        length = 1 
        current_node = head
        
        while current_node.next != None:
            current_node = current_node.next
            length += 1 
        #print("nb elements in the linked list", length)
        
        idx = 1
        current_node = head
        #print ("curr",current_node)
        while idx<= length:
            if (length - n == idx):
                current_node.next = current_node.next.next
                return head
            if (length == n):
                print(current_node)
                return current_node.next
            current_node = current_node.next
            idx += 1

            
            
                
                
        