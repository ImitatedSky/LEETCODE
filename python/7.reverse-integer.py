#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (29.99%)
# Likes:    14013
# Dislikes: 13751
# Total Accepted:    4M
# Total Submissions: 13.2M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#
#
# Example 1:
#
#
# Input: x = 123
# Output: 321
#
#
# Example 2:
#
#
# Input: x = -123
# Output: -321
#
#
# Example 3:
#
#
# Input: x = 120
# Output: 21
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x * (-1)
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x >= 2**31 - 1:
                x = 0
            x = x * (-1)
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x >= 2**31 - 1:
                x = 0
        return x


#
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit
        reversed_x *= sign
        return reversed_x if -(2**31) <= reversed_x <= 2**31 - 1 else 0


# @lc code=end
