"""
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 从后往前遍历，找到第一个比后一个小的数字
        e = len(nums)
        l = len(nums)-2
        while l>=0:
            if nums[l] < nums[l+1]:
                break
            l-=1
        if l == -1:
            nums[:] = nums[::-1]
            return
        # 2. 将后面比这个数字大的第一个数字与这个数字交换
        t = len(nums)-1
        while nums[t]-nums[l]<=0:
            t-=1
        nums[l], nums[t] = nums[t], nums[l]
        # 3。 之后将所有后边的数转置
        l, r = l+1, e-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        

x = Solution()
nums = [1,3,2]
x.nextPermutation(nums)
print(nums)