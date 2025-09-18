#include "Sum of two integers.h"

int Solution::getSum(int a, int b) {
    if (b == 0) {
        return a;
    }
    int sum = a ^ b;
    int carry = a & b;
    int shifted_carry = carry << 1;
    return(Solution::getSum(sum, shifted_carry));
}