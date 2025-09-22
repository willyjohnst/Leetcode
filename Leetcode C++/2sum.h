#include "default lib.h"

class Solution {
private:
    vector<int> twoSum(vector<int>& nums, int target);
public:
    vector<int> checkAnswer(vector<int> a, int b) { return(twoSum(a, b)); };
};