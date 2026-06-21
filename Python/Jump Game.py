class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for idx in range(len(nums)):
            if max_jump < idx:
                return False
            max_jump = max(max_jump, nums[idx] + idx)
        return True

    def canJumpOptimal(self, nums: List[int]) -> bool:
        max_jump = 0

        for idx in range(len(nums)):
            if max_jump < idx:
                return False
            max_jump = max(max_jump, nums[idx] + idx)
            if max_jump >= len(nums) - 1:
                return True
        return True

