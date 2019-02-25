"""
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3

Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

"""
'''
https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code

每次对除数进行移位（乘2）操作，减少时间复杂度
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)  #结果符号位
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1 #*2
                temp <<= 1  #*2
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

x = Solution()
print(x.divide(10, 3))