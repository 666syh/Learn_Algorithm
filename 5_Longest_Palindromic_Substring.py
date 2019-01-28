"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
Example 2:

    Input: "cbbd"
    Output: "bb"
"""
"""
Thanks to Chomohlungma at
https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
        	return s
        maxLen=1
        start=0
        for i in range(1, len(s)):
            #if add a character at the end, the length of longest Palindrome substring may add two 
            
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue
            
            #if add a character at the end, the length of longest Palindrome substring may add one

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

x = Solution()
print(x.longestPalindrome('abccda'))
