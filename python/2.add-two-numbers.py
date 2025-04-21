#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (45.69%)
# Likes:    33206
# Dislikes: 6671
# Total Accepted:    5.6M
# Total Submissions: 12.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#
# Constraints:
#
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
#
#
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            new_cur_next = ListNode(0)
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_cur_next.val = (l1_val + l2_val + carry) % 10

            carry = (l1_val + l2_val + carry) // 10

            current.next = new_cur_next
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


# @lc code=end
