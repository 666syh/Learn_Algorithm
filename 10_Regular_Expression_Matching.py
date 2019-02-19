"""
https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
    Input:
        s = "aa"
        p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input:
        s = "aa"
        p = "a*"
    Output: true
    Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input:
        s = "ab"
        p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
    Input:
        s = "aab"
        p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
    Input:
        s = "mississippi"
        p = "mis*is*p*."
    Output: false
"""
class Solution:
    def isMatch(self, text, pattern):
        #dp数组
        memo = {}
        def dp(i, j):
            #判断是否已经在数组中（之前计算过），若在直接返回
            if (i, j) not in memo:
                #p已遍历完，s是否也遍历完
                if j == len(pattern):
                    ans = i == len(text)
                #若p未遍历完
                else:
                    #假设当前s字符串为：yS
                    #当前p字符串为：xzP
                    #若s也未遍历完，判断x与y是否相等
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    #如果z是‘*’，那么判断P与yS是否匹配或者S和xzP是否匹配
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    #如果z不是‘*’，且x与y相等的话，去掉x与y，判断zP与S
                    else:
                        ans = first_match and dp(i+1, j+1)
                #将判断过的保存在dp数组中
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

x = Solution()
print(x.isMatch("aaa", "a*a"))