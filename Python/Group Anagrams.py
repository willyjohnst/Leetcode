class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for curr in strs:
            anagram_map[tuple(sorted(curr))].append(curr)
        
        list_anagrams = [value for value in anagram_map.values()]
        return list_anagrams

    # So this is good, it works well O(N*K*logK) though because we have to sort the list to hash it
    # So how can we implement this without having to sort it?
    # We can use a list 26 chars long, just add +1 for each char in the string then hash that as a tuple

    def groupAnagramsBetter(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for curr in strs:
            curr_char_list = [0] * 26
            for i in curr:
                curr_char_list[ord(i)-ord('a')] += 1
            anagram_map[tuple(curr_char_list)].append(curr)
        
        list_anagrams = [value for value in anagram_map.values()]
        return list_anagrams

    # We can also implement this without using list comprehension
    def groupAnagramsBest(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for curr in strs:
            curr_char_list = [0] * 26
            for i in curr:
                curr_char_list[ord(i)-ord('a')] += 1
            anagram_map[tuple(curr_char_list)].append(curr)
        
        return list(list_anagrams.values())