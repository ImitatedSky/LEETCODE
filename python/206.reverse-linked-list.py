#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (78.83%)
# Likes:    22751
# Dislikes: 517
# Total Accepted:    5.1M
# Total Submissions: 6.5M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iteratively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        cur = head
        while cur:
            temp = dummy_head.next
            cur_next = cur.next
            dummy_head.next = cur
            dummy_head.next.next = temp
            cur = cur_next

            # here is optimize

            # next_node = cur.next
            # cur.next = dummy_head.next
            # dummy_head.next = cur
            # cur = next_node
        return dummy_head.next


# recursively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 有點箭頭倒轉的概念
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  # 倒轉
        head.next = None  # 切掉原本的
        return new_head


# @lc code=end
