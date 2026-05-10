"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false."""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        startdict = {head.val:head.next}
        curr = head
        while curr is not None:
            # need to check if curr is in startdict, 
            # then check the full path until we get back to this curr.val
            # and if they match the whole way then its true

            # the current node has the same value as a previous node
            # therefore could be the start of a loop
            if curr in startdict:
                # gets the next node from the start of the potential loop
                check = startdict.get(curr)
                # gets the next node from the current node
                loop = curr.next
                # these two need to match for it to be a loop
                while (check == loop):
                    # if we get back to the original value its a loop
                    if (loop == curr):
                        return True
                    # otherwise we just keep going until they either aren't the same
                    # or we get back to the original node (or an identical node in the loop)
                    loop = loop.next
                    check = check.next
            startdict.update({curr:curr.next})
            curr = curr.next

        # Works but only beast 21% of others
        # Can I get it to O(n)?

    def hasCycleOptimal(self, head):
        if head is None or head.next is None:
            return False
        f = head.next
        s = head
        while f and f.next:
            if f == s:
                return True
            f = f.next.next
            s=s.next
        return False
