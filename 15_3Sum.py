"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
"""

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        s = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                a = 0-nums[i]-nums[j]
                if a in nums[j+1:]:
                    l = [nums[i], nums[j], a]
                    l.sort()
                    if l in s:
                        continue
                    s.append(l)
        
        return s


x = Solution()
print(x.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))