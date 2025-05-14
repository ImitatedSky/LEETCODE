#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (35.87%)
# Likes:    12790
# Dislikes: 432
# Total Accepted:    896.3K
# Total Submissions: 2.5M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', return the length
# of the longest valid (well-formed) parentheses substring.
#
#
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
#
#
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        last_valid = -1
        res = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)

            else:
                if stack:
                    stack.pop()
                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        res = max(res, i - last_valid)
                else:
                    last_valid = i
        return res


# @lc code=end
