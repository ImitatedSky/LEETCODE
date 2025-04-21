#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (43.20%)
# Likes:    29786
# Dislikes: 3349
# Total Accepted:    3.3M
# Total Submissions: 7.6M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:

        new_list = nums1 + nums2
        new_list.sort()

        l = len(new_list)
        if l % 2 == 0:
            return (new_list[l // 2 - 1] + new_list[l // 2]) / 2
        else:
            return new_list[l // 2]


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        new_list = []

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                new_list.append(nums2[j])
                j += 1
            else:
                new_list.append(nums1[i])
                i += 1
        # if i < m:
        #     for _ in range(i,m):
        #         new_list.append(nums1[_])
        # if j < n:
        #     for _ in range(j,n):
        #         new_list.append(nums2[_])
        while i < m:
            new_list.append(nums1[i])
            i += 1
        while j < n:
            new_list.append(nums2[j])
            j += 1

        l = len(new_list)
        if l % 2 == 0:
            return (new_list[l // 2 - 1] + new_list[l // 2]) / 2
        else:
            return new_list[l // 2]


# @lc code=end
