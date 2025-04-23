#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.68%)
# Likes:    10925
# Dislikes: 589
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == target:
                    return target
                if abs(_sum - target) < abs(closest - target):
                    closest = _sum
                if _sum < target:
                    l += 1
                else:
                    r -= 1
        return closest


# 想錯 這題是可以隨機取三個數字的
# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         closest  = float("inf")
#         for i in range(len(nums)-2):
#             if sum(nums[i:i+3]) == target:
#                 return target
#             if abs(sum(nums[i:i+3]) -target) < abs(closest-target):
#                 closest = sum(nums[i:i+3])
#         return closest

# @lc code=end
