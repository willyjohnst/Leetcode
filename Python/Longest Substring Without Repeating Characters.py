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
        curr_set = set();
        for right in range(len(s)):
            while s[right] in curr_set:
                curr_set.remove(s[left])
                left += 1;

            curr_set.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength

print(Solution.lengthOfLongestSubstring(Solution, "pwwkew"))