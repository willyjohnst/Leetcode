"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r'[^a-zA-Z]', '', lower(s))        
        stack = []

        print(s)
        # even
        mid = len(s) // 2
        for i in range(mid):
            stack.append(s[i])

        if len(s) % 2 == 1:
            mid += 1
        print(stack)
        print(mid)
        print(len(s) - 1)
        for j in range(mid, len(s)):
            print(s[j])
            c = stack.pop()
            if c != s[j]:
                return False

        return True            

    # better pythonic solution, still memory O(N), need to get to O(1)
    def isPalindromePythonic(self, s):
        import re
        s = re.sub(r'[^a-zA-Z]', '', lower(s))        

        return s == s[::-1]

    # do that by using 2 pointers
    def isPalindromeOptimal(self, s):
        """
        :type s: str
        :rtype: bool
        """
        endptr = len(s) - 1
        startptr = 0
        s = lower(s)

        while startptr < endptr:
            while startptr < len(s) - 1 and not s[startptr].isalnum():
                startptr += 1
            while endptr > -1 and not s[endptr].isalnum():
                endptr -= 1

            if s[startptr] != s[endptr]:
                return False
            startptr += 1
            endptr -= 1

        return True
