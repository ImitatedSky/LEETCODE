#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (36.52%)
# Likes:    41649
# Dislikes: 2014
# Total Accepted:    7.2M
# Total Submissions: 19.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without duplicate
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        _max = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in sub:
                _max = max(
                    _max, i - l + 1
                )  # 其實不應該寫在這，因為做完這個迴圈代表每次sub都是完整的，可以放出來，但寫在這可以少點運算
            else:
                for j in range(l, i + 1):
                    p = sub.pop(0)
                    l += 1
                    if s[i] == p:
                        break
            sub.append(s[i])
        return _max


# 精簡
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        _max = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            _max = max(_max, r - l + 1)
        return _max


# @lc code=end
