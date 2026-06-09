class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        inCurrWindow = defaultdict(int)
        
        maxRepeatStr = 0
        left = 0
        highest_freq = 1                        
        
        for right in range(len(s)):
            inCurrWindow[s[right]] += 1
            highest_freq = max(highest_freq, inCurrWindow[s[right]])

            if (right + 1) - left - highest_freq > k:
                inCurrWindow[s[left]] -= 1
                left += 1
            else:
                maxRepeatStr = max(maxRepeatStr, (right + 1)-left)

        return maxRepeatStr
