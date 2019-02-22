"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        results = []
        self.helper(0, 0, n, '', results)
        return results
    
    def helper(self, l: 'int', r: 'int', n: 'int', s :'str', results: 'List[str]'):
        if s in results:
            return
        if l==n and r==n and s not in results:
            results.append(s)
            return
        t = s
        if l<n:
            s+='('
            l+=1
            self.helper(l, r, n, s, results)
            l-=1
        if r<l and r<n:
            t+=')'
            r+=1
            self.helper(l, r, n, t, results)
            r-=1

x = Solution()
print(x.generateParenthesis(2))