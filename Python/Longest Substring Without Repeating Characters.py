"""Given a string s, find the length of the longest without duplicate characters."""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = 1
        left_ptr = 0
        right_ptr = 0
        curr_window = set()
        while right_ptr < len(s):
            if s[right_ptr] not in curr_window:
                curr_window.add(s[right_ptr])
                right_ptr += 1
            else:
                length = max(length, len(curr_window))
                while s[left_ptr] != s[right_ptr]:
                    curr_window.remove(s[left_ptr])
                    left_ptr += 1
                left_ptr += 1
                right_ptr += 1
        return max(length, len(curr_window))

    # This is technically correct, and works correctly
    # But standand FAANG practice to use for loop to march right pointer along
    # left pointer catch up by using inner while loop

    def lengthOfLongestSubstringFAANGified(self, s):
        if not s:
            return 0
        length = 1
        left_ptr = 0
        char_set = set()
        for char in s:
            while char in char_set:
                char_set.remove(s[left_ptr])
                left_ptr +=1

            char_set.add(s[right_ptr])
            
            length = max(length, len(char_set))

        return length

    # above can be made faster by instead of shrinking the window using the while loop and left pointer
    # we just jump the pointer to the next location using dicts
    def lengthOfLongestSubstringFAANGifiedOptimal(self, s)
        if not s:
            return 0
        char_dict = {}
        length = 1
        left_ptr = 0
        for index, char in enumerate(s):
            if char in char_dict and char_dict[char] >= left_ptr:
                left_ptr = index

            char_dict.update({char:index})
            length = max(length, index - left_ptr)

        return length