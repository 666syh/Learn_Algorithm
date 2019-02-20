"""
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        nums.sort()
        m = 99999
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while(l<r):
                res = nums[i]+nums[l]+nums[r]
                if(abs(target-nums[i]-nums[l]-nums[r])<m):
                    t = res
                    m = abs(target-nums[i]-nums[l]-nums[r])
                if res<target:
                    l+=1
                elif res>target:
                    r-=1
                else:
                    break
            if t == target:
                break
        return t

x = Solution()
print(x.threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0))