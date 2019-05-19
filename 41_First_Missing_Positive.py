"""
https://leetcode.com/problems/first-missing-positive/
"""

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
    Input: [1,2,0]
    Output: 3

Example 2:
    Input: [3,4,-1,1]
    Output: 2

Example 3:
    Input: [7,8,9,11,12]
    Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""




"""
https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
"""
"""
1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
2. we can use the array index as the hash to restore the frequency of each number within 
        the range [1,...,l+1] 
"""
class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)  #凑一个数字，保证余数从1开始，而不是从0开始
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,len(nums)):    #第一个小于n的数就是所求的
            if nums[i]<n:
                return i
        return n

x = Solution()
print(x.firstMissingPositive([2,2]))