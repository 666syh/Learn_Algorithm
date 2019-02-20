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
"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/
backtracking--回溯法（树型结构）
"""
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # 如果后边没有更多的数字
            if len(next_digits) == 0:
                # 将当前的到的结果加入到最终的结果集
                output.append(combination)
            # 如果后边还有数字的话
            else:
                # 迭代这个数字对应的每一个字母
                for letter in phone[next_digits[0]]:
                    # 将每一个字母都加入到之前的字符串之后，进行递归处理
                    backtrack(combination + letter, next_digits[1:])
                    #回溯
                    
        output = []
        if digits:
            backtrack("", digits)
        return output

x = Solution()
print(x.letterCombinations("23"))