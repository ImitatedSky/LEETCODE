#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (56.12%)
# Likes:    20218
# Dislikes: 747
# Total Accepted:    2.4M
# Total Submissions: 4.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# You are given an array of k linked-lists lists, each linked-list is sorted in
# ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#
# Constraints:
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# illegal solution
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # merge all lists into one list
        merge_lists = []
        for i in lists:
            while i:
                merge_lists.append(i.val)
                i = i.next
        merge_lists.sort()

        dummy_head = ListNode(0)
        cur = dummy_head
        for m in merge_lists:
            cur.next = ListNode(m)
            cur = cur.next

        return dummy_head.next


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        def merge_list(l1, l2):
            dummy_head = ListNode(0)
            cur = dummy_head
            while l1 or l2:
                if l1 and l2:
                    if l1.val < l2.val:
                        cur.next = l1
                        l1 = l1.next
                        cur = cur.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                        cur = cur.next
                    continue
                if l1:
                    cur.next = l1
                    l1 = l1.next
                    cur = cur.next
                elif l2:
                    cur.next = l2
                    l2 = l2.next
                    cur = cur.next
            return dummy_head.next

        dummy = ListNode(0)
        for i in lists:
            dummy.next = merge_list(dummy.next, i)
        return dummy.next


# optimized 1
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        def merge_list(l1, l2):
            dummy_head = ListNode(0)
            cur = dummy_head
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2
            return dummy_head.next

        dummy = ListNode(0)
        for i in lists:
            dummy.next = merge_list(dummy.next, i)
        return dummy.next


# divide and conquer
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        def merge_list(l1, l2):
            dummy_head = ListNode(0)
            cur = dummy_head
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2
            return dummy_head.next

        def merge_k_lists(lists, left, right):
            if left == right:
                return lists[left]
            if left < right:
                mid = (left + right) // 2
                left_half = merge_k_lists(lists, left, mid)
                right_half = merge_k_lists(lists, mid + 1, right)
                return merge_list(left_half, right_half)
            return None

        if not lists:
            return None
        return merge_k_lists(lists, 0, len(lists) - 1)


# heap
import heapq


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        min_heap = []
        # 初始化最小堆，把每個鏈表的第一個元素放入堆中
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))

        dummy = ListNode(0)
        current = dummy

        # 堆中元素進行合併
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            # 把當前鏈表的下一個節點放入堆中
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next


# @lc code=end
