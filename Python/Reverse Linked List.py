"""Given the head of a singly linked list, reverse the list, and return the reversed list."""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        dummy = ListNode()
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
    # Code is suboptimal because it is using additional memory for this
    # Best solution uses memory-in-place, so O(1) memory space and O(n) time complexity
    # Instead of saving to dummy, should just use 3 pointers as optimal solution below


    def reverseListOptimial(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        return prev