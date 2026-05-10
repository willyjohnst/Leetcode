"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type."""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
            
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map:
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack
