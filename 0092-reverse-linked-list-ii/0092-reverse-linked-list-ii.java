/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummyNode = new ListNode(0, head);
        ListNode leftPrev = dummyNode;
        ListNode current = head;

        // 1) reach node at position "left"
        for (int i = 0; i < left - 1; i++){
            leftPrev = current;
            current = current.next;
        }

        // Now current="left" and leftPrev="node before left"
        // 2) reverse from left to right
        ListNode prev = new ListNode();
        ListNode temp = new ListNode();
        
        for (int i = 0; i < right - left + 1; i++){
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }

        // 3) Update pointers
        leftPrev.next.next = current;
        leftPrev.next = prev;

        return dummyNode.next;
    }

}