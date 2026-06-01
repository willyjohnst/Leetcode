class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Ok so we have list of words
        # We need to go through the string s and check if the entire string is made of words in the list
        # to do this we can iterate through the string, having a pointer point to the last full word we have
        # I think bredth first search
        # So get a set of pointers to the first char not currently in the list
        # so that way we can have multiple things going at once
        # or DFS is actually probably more standard
        # if we can make a word, then cut it off, and try to make another
            # repeat until we reach the end of the string and have all words, or reach some cut off TBH
        # if not a word, then we keep going 
        # so so use list slice wordDict[currFront] in an inner loop
        
        # Is there a one shot solution? Just go over the string once?
        # start at index 0 with a pointer set to 0 (first full word)
        # then iterate over the list getting s[left:curr]
        # if there is a word found => move left to curr
        # But how then do we deal with the possibility of multiple words being found? 
        # I want to do BFS, so we just keep moving forward along the string
        # So to do that we would need the ability to create multiple pointers
        # Then run a loop over those multiple pointers
        # so like 
        wordSet = set(wordDict)
        ptrSet = {0}
        largest = 0
        for word in wordDict:
            largest = max(largest, len(word))
        for right in range(1,len(s)+1):
            addSet = set()
            removeSet = set()
            for left in ptrSet:
                if s[left:right] in wordSet:
                    if right == len(s):
                        return True
                    # this is wrong, can't be removing left just because we found ONE of the POSSIBLE words in the string
                    # can ONLY remove it when it is IMPOSSIBLE for it to make a word
                    # eg: the letters currently in s[left:right] are in NONE of the words in word set, seems hard to check using a set
                    # dict? no, way too much memory
                    # len(right - left) > len(largest word in wordSet)
                    # can get largest word by iterating through wordDict and taking largest
                    #if left in ptrset:
                    #    ptrset.remove(left)
                    # ALSO, can remove if it makes a word that is already covered
                    addSet.add(right)
                if right - left > largest:
                    removeSet.add(left)
            ptrSet.update(addSet)
            ptrSet -= removeSet
        return False

    # So should either just do it from a stack (while loop)
    # or Dynamic Programming 

    # This implementation is basically the same, but it uses a stack instead of a set
    # If we get the same thing multiple times, will just continue when it reaches there and not reappend it to the stack
    # No need for any fancy method to remove pointers from the set

    def wordBreakStack(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        stack = [0]
        visited = set()

        while stack:
            start = stack.pop()

            if start in visited:
                continue
            visited.add(start)

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    if end == len(s):
                        return True
                    stack.append(end)
        return False

    # That is good, but the more standard way to solve these sorts of questions is using dynamic programming
    # That means we just use a boolean array to represent strings [0:that_index], and they're true if
    # 1) The start is true (so its a valid word up to start)
    # 2) s[start:end] in wordSet
    
    def wordBreakOptimal(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for right in range(1, len(s) + 1):
            for left in range(right):
                if dp[left] and s[left:right] in wordSet:
                    dp[right] = True
                    break

        return dp[len(s)]

