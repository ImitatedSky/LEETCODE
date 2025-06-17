#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (58.83%)
# Likes:    16136
# Dislikes: 419
# Total Accepted:    2.5M
# Total Submissions: 4.2M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            if l.val != r.val:
                return False

            return dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root.left, root.right)


# optimized


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (
                left.val == right.val
                and dfs(left.left, right.right)
                and dfs(left.right, right.left)
            )

        return dfs(root.left, root.right)


# @lc code=end
