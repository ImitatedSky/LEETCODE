#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (62.36%)
# Likes:    14514
# Dislikes: 749
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        n = 0
        dummy_head = ListNode(0, head)
        cur = dummy_head

        while cur.next:
            n += 1
            cur = cur.next

        r = n // k

        cur = dummy_head

        for _ in range(r):
            prev = None  # 新的頭
            tail = cur.next  # 現在這段的頭(之後的尾吧)
            for _ in range(k):
                next_node = cur.next.next
                cur.next.next = prev
                prev = cur.next
                cur.next = next_node
            tail.next = cur.next
            cur.next = prev  # cur.next 新的頭
            cur = tail  # cur 移到尾巴位置

        return dummy_head.next


# optional
class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        cur = dummy_head

        while True:
            tail = cur
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy_head.next

            prev = cur.next
            curr = prev.next
            for _ in range(k - 1):
                prev.next = curr.next
                curr.next = cur.next
                cur.next = curr
                curr = prev.next

            cur = prev


# review
class Solution:
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        n = 0

        while cur.next:
            n += 1
            cur = cur.next
        r = n // k
        cur = dummy_head
        for i in range(r):
            pre = cur
            tail = cur.next
            for _ in range(k):
                move = cur.next
                cur.next = cur.next.next
                move.next = pre.next
                pre.next = move
                cur = tail

        return dummy_head.next


# @lc code=end
