#include <iostream>

using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        /*if (b == 0) {
            return a;
        }
        int sum = a ^ b;
        int carry = a & b;
        int shifted_carry = carry << 1;
        return(getSum(sum, shifted_carry));*/

        while (b != 0) {
            int sum = a ^ b;
            int carry = a & b;
            int shifted_carry = carry << 1;
            a = sum; b = shifted_carry;
        }
        return a;
    }
};

int main() {
    Solution problem;
    int a, b;
    cin >> a;
    cin >> b;
    cout << problem.getSum(a,b);
}