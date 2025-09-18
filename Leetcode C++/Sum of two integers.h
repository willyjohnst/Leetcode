#ifndef SOLUTION_H
#include "default lib.h"

class Solution
{
public:
	int checkAnswer(int a, int b) { return(getSum(a, b)); };
	int getSum(int a, int b);
};
#endif