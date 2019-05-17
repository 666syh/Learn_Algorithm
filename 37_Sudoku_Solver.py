"""
https://leetcode.com/problems/sudoku-solver/
"""
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Note:
    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.
"""

class Solution:

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #深度优先搜索
        self.dfs(board, 0)
    
    def dfs(self, board, num):
        #所有空格均填写完毕
        if num == 81:
            return True
        i, j = num//9, num%9
        #找到下一个非数字
        if board[i][j]!='.':
            return self.dfs(board, num+1)

        flag = []   #记录本格子可以填写那些数字（boolean）
        flag = self.validate(i, j, board)
        for k in range(1, 10):
            #如果可以填写
            if flag[k]:
                board[i][j] = str(k)
                #填写数字之后要保证后边的也可以填写
                if self.dfs(board, num+1):
                    return True
            #如果都不能填写，回溯
        board[i][j] = '.'
        return False
                



    def validate(self, i, j, board):
        flag = [True] * 10
        for k in range(9):
            if board[i][k]!='.':
                flag[int(board[i][k])] = False
            if board[k][j]!='.':
                flag[int(board[k][j])] = False
            r = i//3*3 + k//3
            c = j//3*3 + k%3
            if board[r][c]!='.':
                flag[int(board[r][c])] = False
        
        return flag


        
x = Solution()
g = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

x.solveSudoku(g)
print(g)
