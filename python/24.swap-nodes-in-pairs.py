#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (66.72%)
# Likes:    12444
# Dislikes: 475
# Total Accepted:    1.6M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
#
# Output: [2,1,4,3]
#
# Explanation:
#
#
#
#
# Example 2:
#
#
# Input: head = []
#
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
#
# Output: [1]
#
#
# Example 4:
#
#
# Input: head = [1,2,3]
#
# Output: [2,1,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head

        cur = dummy_head
        i = 0
        while cur and cur.next and cur.next.next:
            nxt = cur.next
            nxt_nxt = cur.next.next if cur.next else None
            if i % 2 == 0:
                cur.next = nxt_nxt
                nxt.next = nxt_nxt.next if nxt_nxt else None
                nxt_nxt.next = nxt

            cur = cur.next

            i += 1
        return dummy_head.next


# optimized
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next

            # swap
            first.next = second.next
            second.next = first
            cur.next = second

            # move cur to the next pair
            cur = first

        return dummy.next


# @lc code=end
