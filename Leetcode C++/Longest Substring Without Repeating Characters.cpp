/*Given a string s, find the length of the longest substring 
without duplicate characters.

 Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
*/
#include "Longest Substring Without Repeating Characters.h"

int Solution::lengthOfLongestSubstring(string s) {
	int left = 0;
	int right = 0;
	int maxLength = 0;
	unordered_set<char> chars;
	while (right != s.size() - 1) { // not at the end of the list
		if (chars.count(s.at(right)) == 0) {
			chars.insert(s.at(right));
			right++;
			int length = right - left;
			if (length > maxLength) {
				maxLength = length;
			}
		}
		else {
			chars.erase(s.at(left));
			left++;
		}
	}
	return(maxLength);
}