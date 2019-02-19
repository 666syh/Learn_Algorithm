"""
https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

[this is a picture]

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""

"""
左边和右边同时向里边移动，哪边小哪边移动
因为如果大的移动的话，那么会越移动越小，而小的移动的话，如果下一个是大的，乘积会增大
https://leetcode.com/problems/container-with-most-water/solution/
"""
class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        m = 0
        i, j = 0, len(height)-1
        while i<j:
            m = max(m, min(height[i], height[j])*(j-i))
            if height[i]<=height[j]:
                i += 1
            else:
                j -= 1
        return m

x = Solution()
print(x.maxArea([1,1]))