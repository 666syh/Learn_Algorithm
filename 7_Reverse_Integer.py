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
正常思维，int->str->int，反转字符串，很慢
"""
"""
class Solution:
    def reverse(self, x: 'int') -> 'int':
        up = -2**31
        if(x < up or x > -up-1):
            return 0
        s = str(x)
        result = ""
        if(x<0):
            result+='-'
            s = s[1:]
        result += s[::-1]
        a = int(result)
        if(a < up or a > -up-1):
            return 0
        return a

x = Solution()
print(x.reverse(0))
"""
"""
int->int faster than before
"""
def reverse(x: 'int') -> 'int':
    result = 0
    if x<0:
        symbol = -1
        x = -x
    else:
        symbol = 1
    while x:
        result = result*10+x%10
        x//=10
    return 0 if result > pow(2, 31) else result * symbol

print(reverse(123))