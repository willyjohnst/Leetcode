/*Given a string s, return the longest substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
*/
#include "Longest Palindromic Substring.h"

int expandAroundCentre(string s, int left, int right) {
	while (left >= 0 && right < s.size() && s.at(left) == s.at(right)) {
		left--; right++;
	}
	return right - left - 1;
}

string Solution::longestPalindrome(string s) {
	if (s.size() <= 2) {
		return s;
	}
	int start = 0;
	int maxLength = 1;
	for (size_t i = 0; i < s.size() - 1; i++) {
		// even palindrome
		int len1 = expandAroundCentre(s, i, i + 1);

		// odd palindrome
		int len2 = expandAroundCentre(s, i, i);

		int currLength = max(len1, len2);
		if (currLength > maxLength) {
			maxLength = currLength;
			start = i - (maxLength - 1) / 2;
		}
	}
	return s.substr(start, maxLength);
}

