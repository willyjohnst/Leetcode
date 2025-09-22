#pragma once
#include "default lib.h"

class Solution {
private:
    int longestConsecutiveON_M(vector<int>& nums);
    
    int longestConsecutive(vector<int>& nums);
public:
    int checkAnswer(vector<int>& nums) { return(longestConsecutive(nums)); };
};