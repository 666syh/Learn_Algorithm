"""
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        i=0
        while i < len(s)//2:
            if(s[i] != s[len(s)-i-1]):
                break
            i+=1
        if i >= len(s)//2:
            return True
        else:
            return False

x = Solution()
print(x.isPalindrome(121))