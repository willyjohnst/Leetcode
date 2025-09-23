"""Given a string s, find the length of the longest

without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, maxLength = 0, 0, 0
        curr_string = {};
        while (right < len(s)):
            if (s[right] not in curr_string):
                curr_string.update({s[right]:s[right]})
                right += 1;
                maxLength = max(maxLength, right - left)
            else:
                curr_string.pop(s[left])
                left += 1;
        return maxLength;

print(Solution.lengthOfLongestSubstring(Solution, "pwwkew"))