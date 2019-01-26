"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        #promise n>=m, so that j>=0 all time, because j = (m+n+1)/2-i
        if(m>n):
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m+n+1)//2
        #search i from [0,m]
        while imin <= imax:
            i = (imin + imax)//2
            j = half_len-i
            if i<m and j>0 and nums2[j-1]>nums1[i]:
                #i is too small, insrease it
                imin = i+1
            elif i>0 and j<m and nums1[i-1]>nums2[j]:
                #i is too big, decrease it
                imax = i-1
            else:
                #i is perfect
                if i==0: max_of_left = nums2[j-1]
                elif j==0: max_of_left = nums1[i-1]
                else: max_of_left = (max(nums1[i-1], nums2[j-1]))
                
                #return derectly when m+n is odd
                if(m+n)%2 == 1:
                    return max_of_left
                
                if i==m: min_of_right = nums2[j]
                elif j==n: min_of_right = nums1[i]
                else: min_of_right = (min(nums1[i], nums2[j]))
                
                #return when m+n is even
                return (min_of_right+max_of_left)/2.0

x = Solution()
print(x.findMedianSortedArrays([1,2], [3,4]))