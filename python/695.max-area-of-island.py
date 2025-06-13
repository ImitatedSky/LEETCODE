#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (72.98%)
# Likes:    10311
# Dislikes: 215
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return
# 0.
#
#
# Example 1:
#
#
# Input: grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected
# 4-directionally.
#
#
# Example 2:
#
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
#
#
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 0

            _res = (
                1
                + dfs(i - 1, j)
                + dfs(i + 1, j)
                + dfs(i, j - 1)
                + dfs(i, j + 1)
            )
            return _res

        for i in range(n):
            for j in range(m):
                res = max(dfs(i, j), res)

        return res


# @lc code=end
