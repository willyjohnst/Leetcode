class Solution:
    def findMinOptimal(self, nums: List[int]) -> int:
        # idea: 
        # left and right pointers
        # left = current left ptr
        # right = current right ptr
        # mid = right - left / 2
        # start left = 0, right = len(nums) - 1
        # eg: [n, n+1, ..., n+m, 1, 2, ..., n-1]
        # if nums[mid] > nums[left] then its not the start of the unrotated sorted list yet, so set left = mid + 1 (can't be mid since mid > left)
        # if nums[mid] < nums[left] then the smallest value is in the front half including mid, so set right = mid
        # repeat this until left >= right

        # I changed to right in the code because as I was sketching out the code, I was comparing to the problem given in example 1: 
        # nums = [0,1,2,4,5,6,7] might become:
        # [4,5,6,7,0,1,2] if it was rotated 4 times.
        # [0,1,2,4,5,6,7] if it was rotated 7 times.
        # I tried comparing left to mid and left to right, then just right to mid
        # I noticed that it actually wouldn't work for left to mid, I would need an additional comparison of right to mid to check.
        # Then I realized I didn't need that comparison at all.
        # So in my notes that was purely theoretical in my head, whereas here it was with an acutal example I saw my mistake.

        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]

        while right > left:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
