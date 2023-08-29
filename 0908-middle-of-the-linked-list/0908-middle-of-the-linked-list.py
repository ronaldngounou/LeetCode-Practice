# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = 0
        current = head 
        while current:
            current = current.next
            size += 1
        print(size)
        cur = head
        count = 0
        while count < size // 2:
            cur = cur.next
            count += 1
        return cur 