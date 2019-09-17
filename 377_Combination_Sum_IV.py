"""
https://leetcode.com/problems/combination-sum-iv/
"""

"""
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.

Example:
    nums = [1, 2, 3]
    target = 4

    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)

    Note that different sequences are counted as different combinations.

    Therefore the output is 7.
"""

# mind 
# dp[i] presents the number of total combinations with target equals to i
# so the result is dp[target]
# dp = 0 initially
# note : if i > num (num in nums): dp[i] += dp[i-num]
# if i == num (num in nums) : dp[i] += 1

class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        for i in range(1, target+1):
            for num in nums:
                if i == num:
                    dp[i] += 1
                elif i > num:
                    dp[i] += dp[i-num]
        return dp[target]

nums = [1, 2, 3]
target = 32
x = Solution()
print(x.combinationSum4(nums, target))
