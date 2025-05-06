#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (44.63%)
# Likes:    6651
# Dislikes: 490
# Total Accepted:    3.3M
# Total Submissions: 7.3M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and i + n < len(haystack) + 1:
                if haystack[i : i + n] == needle:
                    return i

        return -1


# optimized version
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return 0
        for i in range(len(haystack) - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1


# @lc code=end
