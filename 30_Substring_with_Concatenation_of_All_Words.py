"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:
    Input:
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.

Example 2:
    Input:
      s = "wordgoodgoodgoodbestword",
      words = ["word","good","best","word"]
    Output: []
"""
"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13669/99ms-Python-O(kmn)-Solution
用字典来存储words及其个数
"""
class Solution:
    def findSubstring(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if len(words) == 0:
        	return []
	    # initialize d, l, ans
        l = len(words[0])   #每个word的长度
        d = {}              #{words：个数}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        ans = []            #结果集

    	# 外循环l次
        for k in range(l):
            left = k
            subd = {}       #用来保存当前访问过word的字典
            count = 0       #计数器，当计数器=words个数，找到一个满足条件的结果
            #内循环跳着访问，间隔l个
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
    			# valid word
                #将临时访问的word加入到子字典中
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    #如果子字典中某一个word的个数大于目标字典word的个数，这删除字典中之前访问过的word
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)        #加入到结果集中
    			# not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans

x = Solution()
print(x.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))