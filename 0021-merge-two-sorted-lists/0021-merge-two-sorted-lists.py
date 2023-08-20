# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2
        result = ListNode()
        current = result

        while (p1 != None and p2 != None):
            if (p1.val <= p2.val):
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        if (p1 == None):
            current.next = p2
        if (p2 == None):
            current.next = p1
        
        return result.next
