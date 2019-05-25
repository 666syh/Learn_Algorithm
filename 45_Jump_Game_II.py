"""
https://leetcode.com/problems/jump-game-ii/
"""

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
    Input: [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2.
        Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
    You can assume that you can always reach the last index.
"""

"""
from https://leetcode.com/problems/jump-game-ii/discuss/18014/Concise-O(n)-one-loop-JAVA-solution-based-on-Greedy
Greedy
"""
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        curEnd, curFathest = 0, 0
        jumps = 0
        for i in range(len(nums)):
            curFathest = max(curFathest, i+nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFathest
        
                if curEnd>=len(nums)-1:
                    break
        return jumps

        

x = Solution()
print(x.jump([2,3,1,1,4]))           
