"""
https://leetcode.com/problems/combination-sum-ii/
"""

"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
        [1,2,2],
        [5]
    ]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        results = []
        candidates.sort()
        self.search(candidates, target, results, [])
        return results
        
    def search(self, candidates, target, results, result):
        if candidates!=[]:
            for i in range(len(candidates)):
                temp = target
                if candidates[i]<=temp:
                    temp -= candidates[i]
                    if temp == 0:
                        l = result+[candidates[i]]
                        l.sort()
                        if l not in results:
                            results.append(l)
                    else:
                        self.search(candidates[:i]+candidates[i+1:], temp, results, result+[candidates[i]])


x = Solution()
print(x.combinationSum2([1], 8))

#l = [1, 2, 3]
#i = 1
#print(l[:i])
#print(l[i+1:])