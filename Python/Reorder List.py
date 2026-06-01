# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Can I split the list into two, stopping when we meet in the middle
        # so move
        # 1 2 3
        # tmp 5 4 3
        # then it would be easy
        # tmp 1 5 2 4 3 stop here

        # so go through list once to get len
        # then go through again to midpoint
        # then invert back half 
        # then go back to midpoint and merge the two halfs moving both
        if not head.next:
            return head

        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # after that, need to treat back and front as two seperate linked lists
        # and zip them together
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        return head
