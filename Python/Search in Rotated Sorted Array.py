class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # given sorted int array nums with distinct values

        # nums is then left rotated at an unknown index k
        
        # given the k-left rotated int array nums with distinct values
        # return the index of target if it is in nums
            # or -1 if it is not in nums


        # similar to the other one, but instead of trying to find the min
        # trying to find the target: 
        # eg: target is 6
        # [4,5,6,7,0,1,2]
        # if it is greater than/equal to 4 and less than/equal to 7 it is on the left
        # if it is greater than/equal to 7 or less than/equal to 2 it is on the right

        # generalizing:
        # is it and? 
        # yes its and, but there will be 0 numbers when left > mid
        # if the number is less than mid but greater than right: left and mid
        # if the number is less than mid and less than right: mid and right
        # if the number is greater than mid and greater than right: left and mid
        # if the number is greater than mid but less than right: mid and right

        # organize those together:
        # if the number is less than mid but greater than right: left and mid
        # if the number is greater than mid and greater than right: left and mid
        # if the number is less than mid and less than right: mid and right
        # if the number is greater than mid but less than right: could be either?


        # I think I'm entirely wrong and confused.

        # SO starting AGAIN
        # [0 1 2 4 5 6 7]
        # [4 5 6 7 0 1 2]

        # fresh mind, new day coming at it again.
        # so my problem is that if we know mid, left and right it feels like thats not enough information but I think that it being sorted is actually the key
        # so: [ 0 1 2 3 4 5 6 7 ]
        # here if we are searching for x look at 0, 3, and 7
        # [5 6 7 0 1 2 3 4]
        # same thing, searching for x, look at 5, 0, and 4
        # between right and mid: if right > mid then it MUST just be going up between them
        # so if the number is between those two (if target > mid and target <= right): 
            # left = mid + 1
        # else the number is either GREATER than right, or LESS than mid, if its greater than right it must be in the left hand side in a roatated portion
            # if its less than mid, couldn't it still be in the right section? If its less than mid and less than right? Then its the rotated start there
            # if its less than mid and greater than right

        # if target is greater than right AND mid: 
            # 
        # if target is less than right AND target is greater than mid: left = mid + 1
        # else (target is less than right AND less than mid):
            # eg: 5 6 7 1 2 3, target == 2, so target is less than 7 and less than 3 so in this case its right
            # 1 2 3 5 6 7, if target == 2, so target is less than 3 and less than 7 so in this case its left
                # to differentiate if target is less than both: look at right vs mid:
                    # if mid < right: (and target less than both)
                        # right = mid - 1
                    # else (mid > right):
                        # left = mid + 1
        left = 0
        right = len(nums) - 1

        while right > left:
            mid = left + (right - left) // 2
            print(f"nums[{left}]: {nums[left]}, nums[{mid}]: {nums[mid]}, nums[{right}]: {nums[right]}")
            if target == nums[mid]:
                return mid
            if target > nums[right]:
                # THIS LOGIC IS INCORRECT
                # WILL LEAVE IN FOR POST EXAMINATION
                # BUT ITS WRONG, FAILS ON [5,1,3]
                # if target > nums[mid]:
                #     left = mid + 1
                # else:
                #     right = mid - 1

                # so needs two nested too
                if target > nums[mid]:
                    # check if mid > right
                    if nums[mid] > nums[right]:
                        # then we know that if its bigger than mid and right its in [mid:right]
                        left = mid + 1
                    else: # target bigger than both and right > mid
                        right = mid - 1
                else:
                    right = mid - 1
                    
            else: # target < right
                if target < nums[mid]: # so target is less than both right and mid, unknown could be either 
                    if nums[mid] > nums[right]: # mid > right, so all lower values in (mid:right]
                        left = mid + 1
                    else: # mid <= right, so all lower values in [left:mid)
                        right = mid - 1 
                else: # target is less than right and not less than mid
                     left = mid + 1
        if target == nums[left]: 
            return left
        else:
            return -1

        # This logic is technically correct, but very brittle
        # Error prone, difficult to build and understand
        # The key to this problem: Find where the 'cliff' is
        # It will always increase excpet at one point, if you find this point can search the other side of the list
        # Since there is only one of those points it has to be in one half of the list
        # So can check if mid < right, because if the 'cliff' is in the interval (mid, right] then right HAS to be smaller than mid
        # so if right is larger then the cliff is in [left, mid] so we test if target in (mid, right]
            # if yes => left = mid + 1
            # if no => right = mid
        # if right is not larger then the cliff is in (mid,right] so we test if target is in [left, mid)
            # if yes => right = mid - 1
            # if no => left = mid
        
    def searchCliff(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        if nums[left] == target:
            return left
        return -1

    # Thats good, but not quite standard yet
    # The standard implementation uses while left <= right and tests inside the lap
    # If it exits the loop we return -1
    def searchOptimal(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1