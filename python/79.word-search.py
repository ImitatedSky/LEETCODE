#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (44.82%)
# Likes:    16794
# Dislikes: 713
# Total Accepted:    2.1M
# Total Submissions: 4.7M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, word, board):
            if len(word) == 0:
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            temp = board[i][j]
            if temp != word[0]:
                return False

            board[i][j] = "#"
            res = (
                dfs(i - 1, j, word[1:], board)
                or dfs(i + 1, j, word[1:], board)
                or dfs(i, j - 1, word[1:], board)
                or dfs(i, j + 1, word[1:], board)
            )
            board[i][j] = temp
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word, board):
                    return True
        return False


# @lc code=end
