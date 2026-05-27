#Given a string s, return the longest palindromic substring in s.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = s[0]
        for i in range(1, len(s)):
            curr = ""
            # palindrome ...xx...
            if s[i - 1] == s[i]:
                right = i - 1
                left = i
                while left < len(s) and right >= 0 and s[right] == s[left]:
                    curr = s[right] + curr + s[left]
                    left += 1
                    right -= 1
                if len(curr) > len(longest): longest = curr

            # palindrome ..xyx...
            # if both, either could be longer, so need to check both
            curr = ""
            if i - 2 >= 0 and s[i - 2] == s[i]:
                curr = curr + s[i-1]
                right = i - 2 
                while i < len(s) and right >= 0 and s[right] == s[i]:
                    curr = s[right] + curr + s[i]
                    i += 1
                    right -= 1

                if len(curr) > len(longest): longest = curr

        return longest

        # so code works but a few issues with naming and structure
        # it is almost optimal
        # 1) assigning lists like that forces python to construct an enitrely new list every time
        # making the algorithm O(N^3), so technically incorrect
        # 2) I have right and left named the wrong way
        # 3) I am repeating code, so I should pull that out into a helper function
        # 4) I am adjusting the value of i within the while loop, which is bad practice (even in python)

    def longestPalindromeOptimal(self, s):
        longest = s[0]

        def getCurrPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)):
            oddPal = getCurrPalindrome(i, i)
            
            evenPal = getCurrPalindrome(i, i+1)

            if len(oddPal) > len(longest):
                longest = oddPal
            if len(evenPal) > len(longest):
                longest = evenPal
        return longest