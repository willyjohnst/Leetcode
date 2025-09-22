/*Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.*/
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