#ifndef SOLUTION_H
#include "default lib.h"

class Solution {
private:
    int lengthOfLongestSubstring(string s);
public:
    int checkAnswer(string s);
};

int Solution::checkAnswer(string s) {
    return lengthOfLongestSubstring(s);
}
#endif