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
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        '''
        从前往后遍历，但是会错过 s='aaa',p='a*a'
        '''
        '''
        index = 0
        i = 0
        while i < len(p):
            if index >= len(s):
                if p[i] == '*':
                    i+=1
                    continue
                elif i+1<len(p) and p[i+1] == '*':
                    i+=2
                    continue
                else:
                    return False
            if p[i] == s[index] or p[i] == '.':
                i+=1
                index+=1
            elif p[i] == '*':
                i-=1
            else:
                if i+1<len(p) and p[i+1] == '*':
                    i+=2
                else:
                    return False
        if index < len(s):
            return False
        else:
            return True
        '''
        return self.helper(s, 0, p, 0)
        
    def match(self, s, i, p, j):
        #越界，返回false
        if i == len(s) or j == len(p):
            return False
        
        #s[i]和p[j]是否匹配
        return p[j] == '.' or s[i] == p[j]
    
    def helper(self, s, i, p, j):
        # 遍历完毕
        if j == len(p):
            return i == len(s)
        
        if i > len(s):
            return False
        
        # 1. 如果后面字符p[j+1]是*的话,
        #       判断当前字符是否匹配，如果匹配，i+=1
        #           如果不匹配，j+=2
        if j < len(p)-1 and p[j+1] == '*':
            return (self.match(s, i, p, j) and self.helper(s, i+1, p, j)) or self.helper(s, i, p, j+2)
        
        # 2. 当前字符是否匹配，匹配就缩小范围（向后移动）
        if self.match(s, i, p, j):
            return self.helper(s, i+1, p, j+1)
        
        # 3. 无匹配
        return False

x = Solution()
print(x.isMatch("aaa", "a*a"))