"""Given a positive integer n, write a function that returns the number of in its binary representation (also known as the Hamming weight).

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits."""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        numOnes = 0
        for i in range(32):
            if n & 1 == 1:
                numOnes += 1
            n = n >> 1
        return numOnes

class SolutionCache(object):
    def __init__(self):
        self.cache = {}
        for i in range(256):
            self.cache.update(i) = hammingWeight_8_bits(i)

    def hammingWeight_8_bits(self, n):
        numOnes = 0
        for i in range(8):
            if n & 1 == 1:
                numOnes += 1
            n = n >> 1
        return numOnes

    def hammingWeightOptimized(self, n):
        numOnes = 0

        byte0 = n & 0xff
        byte1 = (n >> 8) & 0xff
        byte2 = (n >> 16) & 0xff
        byte3 = (n >> 24) & 0xff

        numOnes += self.cache[byte0]
        numOnes += self.cache[byte1]
        numOnes += self.cache[byte2]
        numOnes += self.cache[byte3]

        return numOnes

class SolutionOptimized(object):
    def hammingWeight(self, n):
        numOnes = 0
        while n != 0:
            numOnes += 1

            n = n & (n - 1)

        return numOnes