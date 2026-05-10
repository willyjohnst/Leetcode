"""Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array."""

# Idea for O(n) time complexity and O(1) space complexity:
# Just do arithmatic sum on x1=0 xn=n d=1, then subtract sum(N)
class Solution(object):
    def missingNumber(self, N):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((len(N)+1)/2.0*len(N)) - sum(N)
