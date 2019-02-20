"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

[this is a picture]

Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        l = len(digits)
        if l==0:
            return []
        if l==1:
            return list(d[digits])
        lt = list(d[digits[0]])
        for i in range(len(digits)-1):
            lt = self.l2l(lt, list(d[digits[i+1]]))
        return lt
        

    def l2l(self, l1:'list', l2:'list'):
        l3 = []
        for i in range(len(l1)):
            for j in range(len(l2)):
                l3.append(l1[i]+l2[j])
        return l3

x = Solution()
print(x.letterCombinations("234"))