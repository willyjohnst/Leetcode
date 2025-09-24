#include "default lib.h"

class Solution {
private:
    string longestPalindrome(string s);
public:
    string checkAnswer(string s) {
        return(longestPalindrome(s));
    }
};