#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.47%)
# Likes:    23195
# Dislikes: 2279
# Total Accepted:    5.2M
# Total Submissions: 7.7M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        cur = dummy_head
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    cur = cur.next
                    list1 = list1.next
                else:
                    cur.next = list2
                    cur = cur.next
                    list2 = list2.next
            elif list1:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        return dummy_head.next


# optimization
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        cur = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        return dummy_head.next


# @lc code=end
