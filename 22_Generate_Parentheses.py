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
"""
https://leetcode.com/problems/generate-parentheses/solution/
backtrack
"""
class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        ans = []
        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2*n:
                ans.append(s)
            if left<n:
                backtrack(s+'(', left+1, right)
            if right<left:
                backtrack(s+')', left, right+1)
        backtrack()
        return ans

x = Solution()
print(x.generateParenthesis(3))