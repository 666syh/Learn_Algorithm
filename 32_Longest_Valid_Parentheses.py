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
1d-dp
pennlio from https://leetcode.com/problems/longest-valid-parentheses/discuss/14141/Pure-1D-DP-without-using-stack-(python)-with-detailed-explanation 
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 一维dp
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # 上一次的结果+2
                    dp[i] = dp[i-2] + 2
                # case 2: (()) 
                # i-dp[i-1]-1 是上一个对应于该 ")" 的 "(" 的索引
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # 前边的右括号已经匹配了 
                    # 之前的匹配数+2，且加上之前可能出现的第一种情况
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # 前边的右括号没有匹配
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now


x = Solution()
print(x.longestValidParentheses(")(())))(())())"))


