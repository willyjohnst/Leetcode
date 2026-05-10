"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice 
(Ignored this to make it harder).

You can return the answer in any order."""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, item in enumerate(nums):
            nums_dict.update({item:index})

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                if nums_dict[diff] != i:
                    return [nums_dict.get(diff), i]