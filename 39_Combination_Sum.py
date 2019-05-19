"""
https://leetcode.com/problems/combination-sum/
"""
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
        [7],
        [2,2,3]
    ]

Example 2:
    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
"""


class Solution:
    def combinationSum(self, candidates, target):
        results = []
        candidates.sort()
        self.search(candidates, target, results, [])
        return results


    def search(self, candidates, target, results, result):
        for i in range(len(candidates)):
            temp = target
            if candidates[i]<=temp:
                temp -= candidates[i]
                if temp == 0:
                    l = result+[candidates[i]]
                    l.sort()
                    if l not in results:
                        results.append(l)
                    break
                else:
                    self.search(candidates, temp, results, result+[candidates[i]])
            else:
                break



x = Solution()
print(x.combinationSum([8,7,4,3], 11))
