class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        listSet = set()
        for num in nums:
            if num in listSet:
                return True
            listSet.add(num)
        return False

    def containsDuplicatePythonic(self, nums):
        return len(set(nums)) != len(nums)