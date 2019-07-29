"""
https://leetcode.com/problems/n-queens-ii/
"""

"""
The n-queens puzzle is the problem of placing n queens 
on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

    Input: 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
"""
class Solution:
    def totalNQueens(self, n):
        def dfs(queue, xy_add, xy_diff):
            result = 0
            p = len(queue)
            if p == n:
                return 1
            for q in range(n):
                if q not in queue and p-q not in xy_diff and p+q not in xy_add:
                    result += dfs(queue+[q], xy_add+[p+q], xy_diff+[p-q])
            return result
        return dfs([], [], [])

x = Solution()
print(x.totalNQueens(4))
            
    
    