"""Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array."""

# Idea for O(n) time complexity and O(1) space complexity:
# Just add all the indices and remainer divison the total by n
# eg: [1, 2, 3, 4, 6], total should be 6/2[1 + 6]=21
class Solution(object):
    def missingNumber(self, N):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((len(N)+1)/2.0*len(N)) - sum(N)

    def missingNumberBest(self, N):
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