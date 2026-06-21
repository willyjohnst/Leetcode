class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sliding and growing window?
        # so when to grow the window?

        # No, its got nothing to do with size, so no need to do it like this
        # I think accordioning window is the way

        # So if its all positives we just keep expanding whole time
        # if its all negatives we just shift the window over at size == 1
        # if its a mix: expand over the positives, and when we get to the negatives, while window_sum > 0, keep expanding it. If window sum becomes negative, then move left to right+1 and right to right+1
        # eg: 1 2 -1 -1 -1 -1 3 4 5
        # [1] => [1, 2] => ... => [1, 2, -1, -1, -1] sum=0 => [-1] => [3] => ... => [3, 4, 5]

        # eg: -8 -3 -1 -5 0 1 4 -2 5 4
        # [-8] => [-3] => [-1] => [-5] => [0] => [1] => [1, 4] => [1, 4, -2] => ... => [1, 4, -2, 5, 4]

        # So just simply if curr_window <= 0, move both left and right to next element, otherwise just keep adding left
        # keep track of max separately

        # I think thats the O(N) solution, 
        # Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

        max_sum = nums[0]
        cur_sum = nums[0]

        for cur_int in nums[1:]:
            if cur_sum <= 0:
                cur_sum = cur_int
            else:
                cur_sum += cur_int
            max_sum = max(max_sum, cur_sum)
        
        return max_sum


    def maxSubArrayDivideAndConquer(self, nums: List[int]) -> int:

        def divide_and_conquer(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            
            max_left = divide_and_conquer(left, mid)
            max_right = divide_and_conquer(mid + 1, right)
            
            curr_sum = 0
            left_cross_max = float('-inf')
            for i in range(mid, left - 1, -1):  
                curr_sum += nums[i]
                left_cross_max = max(left_cross_max, curr_sum)
                
            curr_sum = 0
            right_cross_max = float('-inf')
            for i in range(mid + 1, right + 1): 
                curr_sum += nums[i]
                right_cross_max = max(right_cross_max, curr_sum)
                
            max_cross = left_cross_max + right_cross_max
            return max(max_left, max_right, max_cross)    

        return divide_and_conquer(0, len(nums) - 1)
        


