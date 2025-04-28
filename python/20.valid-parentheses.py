#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.00%)
# Likes:    25592
# Dislikes: 1872
# Total Accepted:    5.9M
# Total Submissions: 14.1M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
#
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
#
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([])"
#
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = [")", "}", "]"]
        mapping = {
            "(": ")",
            ")": "(",
            "{": "}",
            "}": "{",
            "[": "]",
            "]": "[",
        }
        for i in s:
            if stack and i in l and mapping[i] == stack[-1]:
                stack.pop(-1)
                continue
            stack.append(i)

        return True if not stack else False


# optimization
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in mapping:
                if stack and stack[-1] == mapping[i]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False


# @lc code=end
