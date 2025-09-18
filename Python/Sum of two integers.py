class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        boundary = 0x7FFFFFFF

        while (b & mask) != 0:
            bitsum = a ^ b & mask
            carry = a & b
            shifted_carry = carry << 1
            a = bitsum
            b = shifted_carry & mask

        if (a > boundary):
            return ~(a ^ mask)
        return a

print(Solution.getSum(Solution, 15, -4))