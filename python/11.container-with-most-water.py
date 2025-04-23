#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (57.38%)
# Likes:    31026
# Dislikes: 1976
# Total Accepted:    4M
# Total Submissions: 6.9M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
#
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            h = min(height[l], height[r])
            res = max(res, h * (r - l))
            if h == height[l]:
                l += 1
            else:
                r -= 1
        return res


# brute-force solution
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         res = 0

#         for i in range(n):
#             for j in range(n):
#                 if i==j:
#                     continue
#                 h_min = min(height[i],height[j])
#                 res = max(res , (i-j)*h_max)
#         return res

# @lc code=end
