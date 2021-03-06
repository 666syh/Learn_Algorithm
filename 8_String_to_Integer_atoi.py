"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 

Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
    Input: "42"
    Output: 42

Example 2:
    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.Thefore INT_MIN (−231) is returned.
"""
"""
（60ms）
主要是条件一定要找好，不能有漏掉的情况：
    “  +-123 ”  --0
    “  0-1  ”   --0
    “  +0 123”  --0
"""
'''
class Solution:
    def myAtoi(self, str: 'str') -> 'int':
        INT_MAX = 2**31-1
        INT_MIN = -(INT_MAX+1)
        s = str
        result = 0
        symbol = 0
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if start == 0:
                    continue
                else:
                    break
            elif s[i] == '-':
                if start == 1:
                    break
                start = 1
                if symbol == 0:
                    symbol = -1
                    continue
                else:
                    symbol=10
                    break
            elif s[i] == '+':
                if start == 1:
                    break
                start = 1
                if symbol == 0:
                    symbol = 1
                    continue
                else:
                    symbol=10
                    break
            elif s[i]<='9' and s[i]>='0':
                start = 1
                result = result*10+int(s[i])
            else:
                break
        if symbol!=10 and symbol!=0:
            result*=symbol
        elif symbol == 10:
            return 0
        if result > INT_MAX:
            result = INT_MAX
        elif result < INT_MIN:
            result = INT_MIN
        return result

x = Solution()
print(x.myAtoi("   0 123"))
'''
"""
先分割掉空白字符会提升速度（56ms）
"""
def myAtoi(s):
    ls = list(s.strip())
    if len(ls) == 0 : 
        return 0
    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-','+'] : del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit() :
        ret = ret*10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2**31, min(sign * ret,2**31-1))

print(myAtoi(""))