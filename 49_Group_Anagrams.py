"""
https://leetcode.com/problems/group-anagrams/
"""

"""
Given an array of strings, group anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""
class Solution:
    
    def groupAnagrams(self, strs):
        m = {}
        ret = []
        for s in strs:
            l = [] 
            l = list(s)
            l.sort()
            ns = ''.join(l)
            if ns not in m.keys():
                m[ns] = []
            m[ns].append(s)
        for v in m.values():
            ret.append(v)
        return ret

x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))