from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[(len(nums)//2)] + nums[(len(nums)//2)-1])/2
        else:
            return nums[(len(nums)-1)//2]

# class testSolution:
ex1 = Solution()
nums1 = [1, 3]
nums2 = [2]
out1 = ex1.findMedianSortedArrays(nums1, nums2)
print(out1) 
# 2

ex2 = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
out2 = ex2.findMedianSortedArrays(nums1, nums2)
print(out2) 
# 2.5


# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.