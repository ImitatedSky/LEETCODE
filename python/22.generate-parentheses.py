#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.73%)
# Likes:    22050
# Dislikes: 1027
# Total Accepted:    2.3M
# Total Submissions: 3M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        l = n
        r = n

        def backtracking(path, l, r):
            if l == 0 and r == 0:
                res.append(path)
            if l > 0:
                backtracking(path + "(", l - 1, r)
            if r > l:
                backtracking(path + ")", l, r - 1)

        backtracking("", l, r)
        return res


# optimized
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(path, l, r):
            if l == 0 and r == 0:
                res.append(path)
            if l > 0:
                backtracking(path + "(", l - 1, r)
            if r > l:
                backtracking(path + ")", l, r - 1)

        backtracking("", n, n)
        return res


# @lc code=end
