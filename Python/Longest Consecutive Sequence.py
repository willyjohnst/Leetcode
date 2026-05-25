"""Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time."""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                curr_count = 1
                while num + curr_count in num_set:
                    curr_count += 1
                longest = max(longest, curr_count)
        return longest
