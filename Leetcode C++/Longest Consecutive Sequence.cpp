#include "Longest Consecutive Sequence.h"


int Solution::longestConsecutiveON_M(vector<int>& nums) {
    vector<int>count;
    for (size_t i = 0; i < nums.size(); i++) {
        if (count.size() < nums.at(i) + 1) {
            count.resize(nums.at(i) + 1);
        }
        count.at(nums.at(i)) = 1;
    }
    int max_length = 0;
    int curr_length = 0;
    for (size_t i = 0; i < count.size(); i++) {
        if (count.at(i) == 1) {
            curr_length++;
            if (max_length < curr_length) {
                max_length = curr_length;
            }
        }
        else curr_length = 0;
    }
    return max_length;
}
    
int Solution::longestConsecutive(vector<int>& nums) {
    unordered_set<int> s(nums.begin(), nums.end());
    int count = 0;
    int greatest = 0;
    for (size_t i = 0; i < nums.size(); i++) {
        if (!s.count(nums.at(i) - 1)) {
            count = 1;
            int curr_int = nums.at(i);
            while (s.count(curr_int + 1)) {
                count++;
                curr_int++;
            }
            if (count > greatest) greatest = count;
        }
    }
    return (greatest);
}