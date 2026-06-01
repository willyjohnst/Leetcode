class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        backNode = head
        removeNode = head
        forwardNode = head
        while forwardNode:
            forwardNode = forwardNode.next
            if n < 1:
                backNode = removeNode
                removeNode = removeNode.next
            else: 
                n -= 1
        if backNode == removeNode:
            head = head.next
            return head
        
        backNode.next = removeNode.next
        return head

    # This is optimal but we can remove the need for the if statement entirely
    # Use a dummy node instead of head
    # If there is a chance we need to modify the head node of a linked list: Use a dummy node

    def removeNthFromEndDummy(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        removeNode = dummy
        forwardNode = dummy

        while forwardNode:
            forwardNode = forwardNode.next
            if n < 0:
                removeNode = removeNode.next
            else: 
                n -= 1
        
        removeNode.next = removeNode.next.next
        return dummy.next

    # This is good, but we can do it without the if and else statements, 
    # which makes the code cleaner and more readible

    def removeNthFromEndOptimal(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
