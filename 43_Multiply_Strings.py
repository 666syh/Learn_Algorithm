"""
https://leetcode.com/problems/multiply-strings/
"""
"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

Note:
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = self.cul(num1, num2)
        return str(res)
        
    
    def cul(self, num1, num2):
        if num1 == '' or num2 == '':
            return 0
        if num1 == '0' or num2 == '0':
            return 0
        res = 0
        x = int(num1[-1])
        for i in range(len(num2)):
            y = int(num2[-1-i])
            res += x*y*(10**i)
        return res+10*self.cul(num1[:len(num1)-1], num2)

x = Solution()
print(x.multiply('408', '5'))