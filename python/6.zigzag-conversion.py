#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (51.04%)
# Likes:    8406
# Dislikes: 15287
# Total Accepted:    1.7M
# Total Submissions: 3.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = [[] for _ in range(numRows)]
        if numRows == 1 or numRows >= len(s):
            return s  # its could be a edge case

        cur_r = 0
        direct = True

        for i in range(len(s)):
            if direct and cur_r + 1 < numRows:
                row[cur_r].append(s[i])
                cur_r += 1
            elif not direct and cur_r - 1 >= 0:
                row[cur_r].append(s[i])
                cur_r -= 1
            else:
                if cur_r + 1 < numRows:
                    row[cur_r].append(s[i])
                    cur_r += 1
                else:
                    row[cur_r].append(s[i])
                    cur_r -= 1
                direct = not direct

        result = ""
        for r in row:
            result += "".join(r)
        return result


# optimization
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  # its could be a edge case

        result = [""] * numRows
        cur_r = 0
        direct = True

        for i in range(len(s)):
            result[cur_r] += s[i]
            if direct and cur_r + 1 < numRows:
                cur_r += 1
            elif not direct and cur_r - 1 >= 0:
                cur_r -= 1
            else:
                if cur_r + 1 < numRows:
                    cur_r += 1
                else:
                    cur_r -= 1
                direct = not direct

        return "".join(result)


# @lc code=end
