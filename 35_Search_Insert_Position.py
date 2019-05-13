"""
https://leetcode.com/problems/search-insert-position/
"""

"""
Given a sorted array and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""

class Solution:
    def searchInsert(self, nums, target):
        s=0
        n=len(nums)-1
        while(s<n):
            mid = (s+n) // 2
            if(nums[mid]<target):
                s=mid+1
            elif(nums[mid]>target):
                n = mid-1
            else:
                return mid
        if (s==n)&(nums[s]>target):
            return n if s-1>=0 else s
        if (s==n)&(nums[s]<target):
            return n+1
        else:
            return s


x = Solution()
res = x.searchInsert([1,3], 4)
print(res)