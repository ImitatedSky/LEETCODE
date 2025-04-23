#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (29.05%)
# Likes:    12649
# Dislikes: 2277
# Total Accepted:    1.1M
# Total Submissions: 3.9M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
#
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
#
#
#

# @lc code=start
# dynamic-programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            res = False

            if j == len(p):
                return i == len(s)

            first_match = (i < len(s) and j < len(p)) and (
                s[i] == p[j] or p[j] == "."
            )
            # 下一個是 "*"
            if j + 1 < len(p) and p[j + 1] == "*":
                """
                2條路
                1. 直接跳過這
                2. 如果當下有匹配，重複
                """
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res

            return res

        return dp(0, 0)


# 想錯了 正規表達有順序問題 這樣沒解決
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         n = len(s)
#         d = {}

#         for i in range(len(p)):

#             if i == "*":
#                 i+=1
#                 continue
#             if i+1 < len(p) and p[i+1] == "*":
#                 d[p[i]] = n
#                 i+=2
#             else:
#                 d[p[i]] = d.get(p[i], 0) + 1

#         for item in s:
#             if d.get(item, 0)>0:
#                 d[item]-=1
#             elif d.get(".", 0)>0:
#                 d["."]-=1
#             else:
#                 return False
#         return True

# @lc code=end
