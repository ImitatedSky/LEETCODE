#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (36.64%)
# Likes:    32691
# Dislikes: 3077
# Total Accepted:    4.6M
# Total Submissions: 12.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
# O(n²)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                if target - nums[j] in seen:
                    res.add((nums[i], -nums[i] - nums[j], nums[j]))
                seen.add(nums[j])

        return [list(t) for t in res]


# easy to read solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    res.add((nums[i], complement, nums[j]))
                seen.add(nums[j])

        return [list(t) for t in res]


# brute-force solution O(n³)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         res = set()
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if nums[i]+nums[j]+nums[k]==0:
#                         r = tuple(sorted([nums[i],nums[j],nums[k]]))
#                         res.add(r)

#         return [list(t) for t in res]
# @lc code=end
