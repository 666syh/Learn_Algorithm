
"""
https://leetcode.com/problems/permutations/
"""

"""
Given a collection of distinct integers, return all possible permutations.

Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""

# dfs
class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


x = Solution()
print(x.permute([1,2,3,4]))