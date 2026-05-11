"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""
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
        if not list1:
            return list2
        if not list2:
            return list1
        startptr = list1
        if list1.val > list2.val:
            startptr = list2
        curr = startptr
        while list1 and list2:
            # add list2 next
            if list1.val > list2.val:
                tmp = list2
                list2 = list2.next
                curr.next = tmp
            else:
                tmp = list1
                list1 = list1.next
                curr.next = tmp
            curr = curr.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return startptr

    def mergeTwoListsBest():
        def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next