"""
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:
    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"

Example 2:
    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"
"""
'''
stack
zjlvmiao from https://leetcode.com/problems/longest-valid-parentheses/discuss/14141/Pure-1D-DP-without-using-stack-(python)-with-detailed-explanation 
'''
class Solution(object):
    def longestValidParentheses(self, s):
        if not s or len(s) < 2: return 0
        stack = []
        leftmost = -1           #用以记录左边最后一个无用的右括号的位置
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # case ')'
                if not stack: # 如果栈为空，即为无用的右括号
                    leftmost = i
                else:
                    stack.pop() # 删除前方一个左括号的位置
                    if not stack: # 如果栈为空，取当前位置与最后一个无用右括号的距离
                        res = max(res, i - leftmost) 
                    else: # 如果栈不为空，取当前位置与之前第二个左括号的距离
                        a = stack[-1]
                        res = max(res, i - stack[-1]) 
        return res


x = Solution()
print(x.longestValidParentheses(")(())))(())())"))


