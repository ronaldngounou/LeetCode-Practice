# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Create 2 strings that we are going to convert into integers and do the sum. 
        current_node = l1
        num1 = ""
        num2 = ""
        
        #we loop until the node before the last node
        while current_node.next != None:
            num1 += str(current_node.val) 
            #convert the value in the node into a string.
            current_node = current_node.next 
            #we set the current_node to be the next node.
        num1 += str(current_node.val) 
        #for the last node, we add it separetely outside of the for loop
        
        #we repeat the same operation for the second number.
        
        current_node = l2
        while current_node.next != None:
            num2 += str(current_node.val)
            current_node = current_node.next
        num2 += str(current_node.val)
        
        res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        # After we sum, we will convert the integers into a string because it's easier to manipulate for linkedlists.
        
        #We create the head of the linkedlist, called linkedlist.
        linkedlist = ListNode(val=res[0])
        current_node = linkedlist
        
        idx = 1 #initalize the index before the while loop
        while idx < len(res):
            current_node.next = ListNode(val = res[idx])
            current_node = current_node.next
            idx += 1
         #Finally we return the head of the list. As we return the head, the whole list will be returned. 
        
        return linkedlist # as we return the head of the linkedlist, the whoe list will be changed
        