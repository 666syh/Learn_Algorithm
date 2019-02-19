"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string .

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""
'''
prefix--前缀
'''
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        '''
        纵向比较法：从第一个字母开始比较每一个单词的每一个字母
        '''
        if len(strs) == 0:
            return ""
        i = 0
        while i<len(strs[0]):
            #取第一个的单词的第一个字母
            t = strs[0][i]
            j = 1
            #拿后边每一个单词的同一位置上的字母进行比较
            while j<len(strs):
                if i==len(strs[j]) or t != strs[j][i]:
                    break
                j+=1
            if j<len(strs):
                break
            i+=1
        if i == 0:
            return ""
        return strs[0][:i]

x = Solution()
print(x.longestCommonPrefix(["aa", "a"]))