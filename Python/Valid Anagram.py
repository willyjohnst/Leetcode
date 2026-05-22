class Solution(object):
    def __init__(self):
        from string import ascii_lowercase
        self.inList = dict(zip(ascii_lowercase, [0]*26))
        
        
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        self.addChars(s)
         
        if self.checkChars(t):
            return True
        return False

    def addChars(self, s):
        for l in s:
            self.inList[l] += 1

    def checkChars(self, t):
        for l in t:
            self.inList[l] -= 1
        for l in list(self.inList):
            if self.inList[l] != 0:
                return False
        return True

    # Solution is very messy, can be a lot simpler.
    # Don't need a class wide variable in inList, can just have local variable
    # Local variable is actually preferable

    def isAnagramOptimal(self, s, t):
        from string import ascii_lowercase
        chars_s = dict(zip(ascii_lowercase, [0]*26))

        if len(s) != len(t):
            return False

        for l in s:
            chars_s[l] += 1

        for l in t:
            chars_s[l] -= 1

        for count in chars_s.values():
            if count != 0:
                return False
        return True

