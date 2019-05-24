"""
https://leetcode.com/problems/wildcard-matching/
"""

"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
    Input:
        s = "aa"
        p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input:
        s = "aa"
        p = "*"
    Output: true
    Explanation: '*' matches any sequence.

Example 3:
    Input:
        s = "cb"
        p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
    Input:
        s = "adceb"
        p = "*a*b"
    Output: true
    Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

    Input:
        s = "acdcb"
        p = "a*c?b"
    Output: false
"""


"""
from https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.com(s, p)

    def com(self, s, p):
        s_start, p_start = 0, 0
        match = 0
        startID = -1
        while(s_start<len(s)):
            #s的一个字符与p的一个字符或？匹配
            if p_start<len(p) and (p[p_start] == "?" or p[p_start] == s[s_start]):
                s_start += 1
                p_start += 1
            #匹配*
            elif p_start<len(p) and p[p_start] == "*":
                startID = p_start
                match = s_start
                p_start += 1
            elif startID != -1:
                p_start = startID+1
                match += 1
                s_start = match
            else:
                return False
        while(p_start<len(p) and p[p_start] == "*"):
            p_start += 1
        return p_start == len(p)
    

x = Solution()
print(x.isMatch("acaa", "a*a"))   