#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (58.72%)
# Likes:    4597
# Dislikes: 258
# Total Accepted:    522.4K
# Total Submissions: 888.3K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5
#
#
#
# Note: This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self._res = float("inf")
        self._pre = None

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if self._pre is not None:
                self._res = min(self._res, node.val - self._pre.val)

            self._pre = node
            dfs(node.right)

            return self._res

        return dfs(root)


# @lc code=end
