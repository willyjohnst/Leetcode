#pragma once
#include "default lib.h"

class Solution {
public:
    int longestConsecutiveON_M(vector<int>& nums);
    
    int longestConsecutive(vector<int>& nums);

    int checkAnswer(vector<int>& nums) { return(longestConsecutive(nums)); };
};