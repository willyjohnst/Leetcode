"""You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""
class Solution(object):
    def __init__(self):
        self.cacheSteps = {}
        self.cacheSteps[0] = 0
        self.cacheSteps[1] = 1
        self.cacheSteps[2] = 2

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.cacheSteps.get(n):
            return self.cacheSteps[n]

        if n - 2 >= 0:
            if not self.cacheSteps.get(n-1):
                self.cacheSteps[n - 1] = self.climbStairs(n - 1)
            if not self.cacheSteps.get(n-2):
                self.cacheSteps[n - 2] = self.climbStairs(n - 2)
            return self.cacheSteps[n - 1] + self.cacheSteps[n - 2]
        # This code is suboptimal because:
        # 1) The n - 2 is redundant; 0, 1, and 2 are in the cache already so we don't need this check, it will never fail
        # 2) if not self.cacheSteps.get(n-1) is redundant too, we don't need the value here, we aren't doing anything with it
            # instead, should just check if n-1 in self.cacheSteps
        # 3) The checks are redundant too => checking if its in there alreday is done line 23
            # So we don't need those checks at all
        # 4) We can combine the 2 cacheSteps statements into 1 (as below)
            # It is better because code is cleaner
        # below is WAY cleaner

    def climbStairsOptimal(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cacheSteps:
            return self.cacheSteps[n]

        self.cacheSteps[n] = self.climbStairsOptimal(n - 1) + self.climbStairsOptimal(n - 2)
        
        return self.cacheSteps[n]
