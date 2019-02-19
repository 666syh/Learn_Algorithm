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
"""
从两个端点到中间遍历，且跳过重复数据，减少时间复杂度
"""
class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        res = []
        #先将数组排序
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            #因为数组已经排好序，三个正数相加不可能等于0
            if nums[i]>0: 
                break 
            #相同的i跳过
            if i>0 and nums[i]==nums[i-1]: 
                continue 
            #分别从两头向中间靠拢
            l, r = i+1, length-1 
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                #如果总数小了，则提高l
                if total<0: 
                    l+=1
                #如果总数大了，则减小r
                elif total>0: 
                    r-=1
                else: 
                    #加入进结果集中
                    res.append([nums[i], nums[l], nums[r]])
                    #跳过相同元素
                    while l<r and nums[l]==nums[l+1]: 
                        l+=1
                    while l<r and nums[r]==nums[r-1]: 
                        r-=1
                    l+=1
                    r-=1
        return res

x = Solution()
print(x.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))