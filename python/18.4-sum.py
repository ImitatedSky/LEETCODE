#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (37.78%)
# Likes:    11965
# Dislikes: 1457
# Total Accepted:    1.2M
# Total Submissions: 3.3M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    complement = target - nums[i] - nums[j] - nums[k]
                    if complement in seen:
                        res.add((nums[i], nums[j], complement, nums[k]))
                    seen.add(nums[k])

        return [list(r) for r in res]


# brute-force solution O(n⁴)
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()

#         n = len(nums)
#         res = set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     for l in range(k+1,n):
#                         if nums[i] + nums[j] + nums[k] + nums[l] == target:
#                             res.add((nums[i],nums[j],nums[k],nums[l]))
#         return [list(r) for r in res]


# @lc code=end
