"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 

Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=0
        for i in range(len(s)):
            j = i
            l = []
            while(j<len(s)):
                if(s[j] not in l):
                    l.append(s[j])
                else:
                    break
                j+=1
            le = j-i
            if(le>k):
                k = le

        return k

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
好的解法，O（n）
"""
def lengthOfLongestSubstring(s):
    start = maxLength = 0   #start为子字符串起始位置，maxLength记录最大长度
    usedChar = {}           #字典，记录子字符串中每个字符及其位置
    for i in range(len(s)):
        if s[i] in usedChar and start<=usedChar[s[i]]:
            start = usedChar[s[i]]+1
        else:
            maxLength = max(maxLength, i-start+1)
        
        usedChar[s[i]] = i
    return maxLength