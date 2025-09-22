/*Given an array of integers nums and an integer target
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/
#include "2sum.h"

vector<int> Solution::twoSum(vector<int>& nums, int target) {
	unordered_map<int, int> count;
	for (int val : nums) {
		count[val]++;
	}

	for (pair<int, int>val: count) {
		int difference = target - val.first;
		int difference_count = count.count(difference);
		if ((difference_count == 1) || (val.second > 1 && difference == target)) {
			vector<int>a = { val.first, difference };
			return(a);
		}
	}
	vector<int> c{ -1, -1 };
	return(c);
}