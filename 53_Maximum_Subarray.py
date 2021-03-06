"""
https://leetcode.com/problems/maximum-subarray/
"""
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    
Follow up:

If you have figured out the O(n) solution, try coding another solution 
using the divide and conquer approach, which is more subtle.
"""
# O(n)
class Solution:
    def maxSubArray(self, nums):
        maxsum = nums[0]
        if len(nums)>1:
            for i in range(1, len(nums)):
                if nums[i]+nums[i-1] > nums[i]:
                    nums[i] += nums[i-1]
                if maxsum < nums[i]:
                    maxsum = nums[i]
        return maxsum
                    

x = Solution()
print(x.maxSubArray([1,2]))
        
