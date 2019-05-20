"""
https://leetcode.com/problems/trapping-rain-water/
"""

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

[picture]

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


"""
from https://leetcode.com/problems/trapping-rain-water/discuss/17357/Sharing-my-simple-c%2B%2B-code%3A-O(n)-time-O(1)-space
"""
class Solution:
    def trap(self, height):
        left, right = 0, len(height)-1
        res = 0
        maxleft, maxright = 0, 0
        while(left<=right):
            if height[left]<height[right]:
                if height[left]>=maxleft:
                    maxleft = height[left]
                else:
                    res+=maxleft-height[left]
                left+=1
            else:
                if height[right]>=maxright:
                    maxright = height[right]
                else:
                    res+=maxright-height[right]
                right-=1
        return res

                
x = Solution()
l = [5,2,1,2,1,5]
print(x.trap(l))