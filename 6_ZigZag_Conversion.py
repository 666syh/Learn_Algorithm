"""
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""

class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        result = ""
        if numRows == 1:
            result = s
            return result
        length = len(s)
        n = 2*numRows - 2
        #遍历每一行
        for i in range(numRows):
            index = i
            #搜索下一个字符
            while index < length:
                if(i==0 or i==numRows-1):
                    result += s[index]
                    index += n
                else:
                    result += s[index]
                    index += n-2*i
                    if(index >= length):
                        break
                    result += s[index]
                    index += 2*i
        return result

x = Solution()
print(x.convert("A", 1))