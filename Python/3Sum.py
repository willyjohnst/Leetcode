class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # a + b then requires c to be in the list
        # can check quickly using sets
        # thats O(N^2), probably not fast enough though
        # so get list [a, b, c, ..., zz] and set {a, b, c, ..., zz}
        # start at a, add b check if - (a + b) belongs to the set?
        # Same algorithm as above

        # If I sort the list, then I could skip checks, but I can't
        # OH I will start with the smallest # and go up maybe? So if I am starting with a larger number, I will already have done any options with smaller numbers so skip
        # But that still requires me to sort it
        # is there a way to do this without sorting it?
        # yes, I can remove it from the set after I have checked all the items

        # So for a: check a + b, a + c, a + ..., a + zz
        # If any of them are solutions append them to the list
        # Then remove a from the set, there are no unseen solutions containing a
        # repeat for all elements until zz

        # So could do it using a set
        # Also do it using maybe just a stack?
        # I think I will just let nums be a stack 
        # To save on memory

        # instead of a dict
        # will use dp
        # where true = this number is in nums
        # seems like a waste of memory actually, would need to be max(nums) long
        # instead just do a set?
        # no same problem as before, so will have to uncomment NumsDict out
        # dp = [False] * len(nums)

        # actually just do two sets
        # 1) contains all the possible values of nums, O(1) finding third
        # 2) checks if we already have this set
        # no no, this doesn't quite work still, because of duplicate values
        # So still have to do the dict (for now) for 1
        # 2 still good though

        #numsSet = {nums}
        
        """numsDict = {}
        for idx, num in enumerate(nums):
            numsDict[num] = idx

        for i in range(len(nums)):
            first = nums.pop()
            for j in range(len(nums)):
                if len(nums) - 1 == j:
                    continue
                second = nums[j]
                # wait this might be a problem
                # can triple count a set
                # we start with c, then remove it from nums
                # but it stays in thirdSet
                # but we can't remove it from thirdSet because we need it
                # could do a dict where we have the val = # of times that value is in the triple
                third = - (first + second) 
                if NumsDict.get(second) > 0 and \
                    third in NumsDict and NumsDict.get(third) > 0:
                        if second == third:
                            if NumsDict.get(third) == 1:
                                continue
                        triplets.append([first, second, third])
            NumsDict[first] -= 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                first = nums[i]
                second = nums[j]
                third = -(first + second)
                if third in numsDict and numsDict[third] != i and numsDict[third] != j:
                    # its a triplet
                    # need to check if its a unique triplet
                    # very annoying I can't do sets of sets
                    # could just iterate through solutions
                        # hate that though, deffo way too slow
                    # could I keep a queue of potential matches?
                    # nah I don't think so
                    # guess I will just iterate through solutions for now
                    unique = True
                    for solution in triplets:
                        print({first, second, third}, set(solution))
                        if {first, second, third} & set(solution) == {first, second, third} | set(solution):
                            unique = False
                            break
                    if unique:
                        triplets.append([first,second,third])
                # I need some way to check that I haven't got this triplet already
                # So I have a b c and need to check (a c b), (c a b), (c b a)
                # could get a set of all the unique (a,b) pairings?"""

        # So idea
        # Sort list then set a pointer first for the first element
        # check if we have seen it before (if s[first -1] == s[first]: continue)
        # then we havent seen it before, so use a front and back pointer
        # if sum > 0 move right pointer -1, if sum < 0, move left pointer
        # if sum == 0 and s[left - 1] != s[left] and s[right -1] != s[right]: triplets.append([first, s[left], s[right]])
        # then return triplets

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            while right > left:
                total = a + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                    continue
                if total < 0:
                    left += 1
                    continue
                triplets.append([a, nums[left], nums[right]])
                while right > left and nums[left] == nums[left + 1]:
                    left += 1
                while right > left and nums[right] == nums[right - 1]:
                    right -=1
                left += 1
                right -= 1                
        return triplets


    def threeSumOptimal(self, nums: list[int]) -> list[list[int]]:
        # a + b then requires c to be in the list
        # can check quickly using sets
        # thats O(N^2), probably not fast enough though
        # so get list [a, b, c, ..., zz] and set {a, b, c, ..., zz}
        # start at a, add b check if - (a + b) belongs to the set?
        # Same algorithm as above

        # If I sort the list, then I could skip checks, but I can't
        # OH I will start with the smallest # and go up maybe? So if I am starting with a larger number, I will already have done any options with smaller numbers so skip
        # But that still requires me to sort it
        # is there a way to do this without sorting it?
        # yes, I can remove it from the set after I have checked all the items

        # So for a: check a + b, a + c, a + ..., a + zz
        # If any of them are solutions append them to the list
        # Then remove a from the set, there are no unseen solutions containing a
        # repeat for all elements until zz

        # So could do it using a set
        # Also do it using maybe just a stack?
        # I think I will just let nums be a stack 
        # To save on memory

        # instead of a dict
        # will use dp
        # where true = this number is in nums
        # seems like a waste of memory actually, would need to be max(nums) long
        # instead just do a set?
        # no same problem as before, so will have to uncomment NumsDict out
        # dp = [False] * len(nums)

        # actually just do two sets
        # 1) contains all the possible values of nums, O(1) finding third
        # 2) checks if we already have this set
        # no no, this doesn't quite work still, because of duplicate values
        # So still have to do the dict (for now) for 1
        # 2 still good though

        #numsSet = {nums}
        
        """numsDict = {}
        for idx, num in enumerate(nums):
            numsDict[num] = idx

        for i in range(len(nums)):
            first = nums.pop()
            for j in range(len(nums)):
                if len(nums) - 1 == j:
                    continue
                second = nums[j]
                # wait this might be a problem
                # can triple count a set
                # we start with c, then remove it from nums
                # but it stays in thirdSet
                # but we can't remove it from thirdSet because we need it
                # could do a dict where we have the val = # of times that value is in the triple
                third = - (first + second) 
                if NumsDict.get(second) > 0 and \
                    third in NumsDict and NumsDict.get(third) > 0:
                        if second == third:
                            if NumsDict.get(third) == 1:
                                continue
                        triplets.append([first, second, third])
            NumsDict[first] -= 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                first = nums[i]
                second = nums[j]
                third = -(first + second)
                if third in numsDict and numsDict[third] != i and numsDict[third] != j:
                    # its a triplet
                    # need to check if its a unique triplet
                    # very annoying I can't do sets of sets
                    # could just iterate through solutions
                        # hate that though, deffo way too slow
                    # could I keep a queue of potential matches?
                    # nah I don't think so
                    # guess I will just iterate through solutions for now
                    unique = True
                    for solution in triplets:
                        print({first, second, third}, set(solution))
                        if {first, second, third} & set(solution) == {first, second, third} | set(solution):
                            unique = False
                            break
                    if unique:
                        triplets.append([first,second,third])
                # I need some way to check that I haven't got this triplet already
                # So I have a b c and need to check (a c b), (c a b), (c b a)
                # could get a set of all the unique (a,b) pairings?"""

        # So idea
        # Sort list then set a pointer first for the first element
        # check if we have seen it before (if s[first -1] == s[first]: continue)
        # then we havent seen it before, so use a front and back pointer
        # if sum > 0 move right pointer -1, if sum < 0, move left pointer
        # if sum == 0 and s[left - 1] != s[left] and s[right -1] != s[right]: triplets.append([first, s[left], s[right]])
        # then return triplets

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            while right > left:
                total = a + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                    continue
                if total < 0:
                    left += 1
                    continue
                triplets.append([a, nums[left], nums[right]])
                while right > left and nums[left] == nums[left + 1]:
                    left += 1
                while right > left and nums[right] == nums[right - 1]:
                    right -=1
                left += 1
                right -= 1                
        return triplets 
