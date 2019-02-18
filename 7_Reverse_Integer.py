"""
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""
"""
正常思维，反转字符串，很慢
"""
class Solution:
    def reverse(self, x: 'int') -> 'int':
        up = -2**31
        down = 2**31-1
        if(x < up or x > down):
            return 0
        s = str(x)
        result = ""
        if(x<0):
            result+='-'
            s = s[1:]
        result += s[::-1]
        a = int(result)
        if(a < up or a > down):
            return 0
        return a

x = Solution()
print(x.reverse(0))