"""
https://leetcode.com/problems/n-queens/
"""

"""
The n-queens puzzle is the problem of placing n queens 
on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
    Input: 4
    Output: [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

# 352ms
# class Solution:
#     def solveNQueens(self, n):
#         matrix = []
#         for i in range(n):
#             matrix.append([])
#             for j in range(n):
#                 matrix[i].append('.')
#         ret = []
#         self.search(matrix, n, 0, ret)
#         return ret

#     def search(self, matrix, n, i, ret):

#         for j in range(n):
#             if matrix[i][j] == '.' and self.canPlace(matrix, n, i, j):
#                 matrix[i][j] = 'Q'
#                 if i == n-1:
#                     m = []
#                     for k in range(n):
#                         l = "".join(matrix[k])
#                         m.append(l)
#                     ret.append(m)
#                     matrix[i][j] = '.'
#                     return
#                 self.search(matrix, n, i+1, ret)
#                 matrix[i][j] = '.'
#             else:
#                 continue
#         return

#     def canPlace(self, matrix, n, i, j):
#         for k in range(-n+1, n):
#             if k>=0 and (matrix[i][k] == 'Q' or matrix[k][j] == 'Q'):
#                 return False
#             if i+k>=0 and j+k>=0 and i+k<n and j+k<n and matrix[i+k][j+k] == 'Q':
#                 return False
#             if i-k>=0 and j+k>=0 and i-k<n and j+k<n and matrix[i-k][j+k] == 'Q':
#                 return False
#         return True
                
# x = Solution()
# print(x.solveNQueens(3))

"""
https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
"""

def solveNQueens(n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            # 用p-q代表左斜对角线上的所有点，p+q代表右斜对角线上的所有点
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                # 用形参的方式回溯
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    # result中的每个元素的每一个数字代表Q在该行的第几列
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

print(solveNQueens(4))