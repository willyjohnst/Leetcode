"""Reverse bits of a given 32 bits signed integer.

Example 1:
Input: n = 43261596
Output: 964176192

Explanation:
Integer	    Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
"""
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result = result << 1
            result = result | n & 1
            n = n >> 1
        return result

class SolutionOptmized(object):
    def __init__(self):
        self.cache = {}
        for i in range(256):
            self.cache[i] = self.reverse_8_bits(i)

    def reverse_8_bits(self, n):
        result = 0
        for i in range(8):
            result = result << 1
            result = result | (n & 1)
            n = n >> 1
        return result

    def reverseBitsOptimized(self, n):
        """
        :type n: int
        :rtype: int
        """
        byte0 = n & 0xff
        byte1 = (n >> 8) & 0xff
        byte2 = (n >> 16) & 0xff
        byte3 = (n >> 24) & 0xff

        rev0 = self.cache.get(byte0)
        rev1 = self.cache.get(byte1)
        rev2 = self.cache.get(byte2)
        rev3 = self.cache.get(byte3)

        return (rev0 << 24) | (rev1 << 16) | (rev2 << 8) | rev3
