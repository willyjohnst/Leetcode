class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ldict = {x: x for x in nums}
        curr_count = 0;
        max_count = 0;
        for i in nums:
            if (i - 1 not in ldict):
                curr_int = i;
                while (curr_int in ldict):
                    curr_count += 1
                    curr_int += 1
                if (curr_count > max_count):
                    max_count = curr_count
                curr_count = 0
        return max_count
