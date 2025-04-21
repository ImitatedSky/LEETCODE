#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (35.47%)
# Likes:    30560
# Dislikes: 1887
# Total Accepted:    3.7M
# Total Submissions: 10.5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            # odd
            l = i
            r = i
            while -1 < l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1

            # even
            l = i
            r = i + 1
            while -1 < l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
        return res


# @lc code=end
