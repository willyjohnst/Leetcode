"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice 
(Ignored this to make it harder).

You can return the answer in any order."""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ldict = {}
        for index, value in enumerate(nums):
            if (ldict.__contains__(value)):
                ldict[value].append(index)
            else:
                ldict[value] = [value]

        for curr in nums:
            difference = target - curr;
            # either target is different to difference or there are multiple targets in the list
            if (curr != difference or len(ldict.get(difference)) > 1):
                if (difference in ldict):
                    return([curr, difference])
