import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        currList = list()

        for curr in nums:
            listIdx = bisect_left(currList, curr)
            if listIdx == len(currList):
                currList.append(curr)
            else:
                currList[listIdx] = curr

        return len(currList)

    def lengthOfLIS_Binary_insert(self, nums: List[int]) -> int:
        currList = [nums[0]]

        def binary_insert(currList, target):
            left = 0
            right = len(currList) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if currList[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        for curr in nums[1:]:
            listIdx = binary_insert(currList, curr)
            if listIdx == len(currList):
                currList.append(curr)
            else:
                currList[listIdx] = curr
        return len(currList)
