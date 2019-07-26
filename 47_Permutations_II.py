"""
https://leetcode.com/problems/permutations-ii/
"""
"""
Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.

Example:
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
"""

class Solution:
    def permuteUnique(self, nums):
        nums = sorted(nums)
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
            return
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], ret)
    
x = Solution()
print(x.permuteUnique([1, 1]))