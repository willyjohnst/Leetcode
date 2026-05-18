"""Given an integer n, 
return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
"""
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n+1):
            counter = 0
            while i > 0:
                if i & 1:
                    counter += 1
                i = i >> 1
            ans.append(counter)
        
        return ans
