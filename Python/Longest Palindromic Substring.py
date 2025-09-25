class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (not s):
            return ""
        
        start = 0
        maxLength = 1
        for i in range(len(s)):
            len1 = self.expandAroundCentre(s, i, i) #odd
            len2 = self.expandAroundCentre(s, i, i + 1) #even

            currLength = max(len1, len2)
            if currLength > maxLength:
                maxLength = currLength
                start = i - int((maxLength - 1) / 2)
        return s[start:start+maxLength];

    def expandAroundCentre(self, s: str, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return right - left - 1



sol = Solution() 
print(sol.longestPalindrome("babad"))