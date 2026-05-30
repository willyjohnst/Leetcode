class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def countCurrPalindrome(left, right):
                count = 0
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                return count

        # add each individual char to begin
        count = len(s)
        for i in range(len(s)):
            # odd palindrome 
            if i+1 < len(s) and s[i] == s[i+1]:
                count += countCurrPalindrome(i, i+1)
            # even palindrome
            if i+2 < len(s) and s[i] == s[i+2]:
                count += countCurrPalindrome(i, i+2)
        return count

        # code above works correctly but theres a few things that need fixing
        # 1) bit weird to add len(s) to count at the start (though it is more efficient)
        # 2) if statements are redundent, checking that again in the while loop
        # Fixed in code below

        def countCurrPalindromeOptimal(left, right):
                count = 0
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                return count

        # add each individual char to begin
        count = 0
        for i in range(len(s)):
            # odd palindrome 
            count += countCurrPalindromeOptimal(i, i)
            # even palindrome
            count += countCurrPalindromeOptimal(i, i+1)
        return count
