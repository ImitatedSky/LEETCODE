#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (61.60%)
# Likes:    6011
# Dislikes: 296
# Total Accepted:    519.7K
# Total Submissions: 843.5K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
#
#
# Example 2:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
#
#
# Example 3:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
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
# Follow up: Could you solve it without reversing the input lists?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# dfs
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def dfs(n1, n2):
            if not n1 and not n2:
                return None, 0
            next_node = None
            carry = 0

            if n1.next and n2.next:
                next_node, carry = dfs(n1.next, n2.next)
            # elif n1.next:
            #     next_node , carry = dfs(n1.next,n2)
            # elif n2.next:
            #     next_node , carry = dfs(n1,n2.next)
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            _sum = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            node = ListNode(_sum)
            node.next = next_node
            return node, carry

        def get_length(node):
            d = 0
            while node:
                d += 1
                node = node.next
            return d

        def set_pad(node, l):
            dummy_head = ListNode(0)
            dummy_head.next = node
            while l:
                l -= 1
                new_head = ListNode(0)
                new_head.next = dummy_head.next
                dummy_head.next = new_head
            return dummy_head.next

        l1l = get_length(l1)
        l2l = get_length(l2)
        if l1l > l2l:
            l2 = set_pad(l2, l1l - l2l)
        elif l2l > l1l:
            l1 = set_pad(l1, l2l - l1l)
        node, _carry = dfs(l1, l2)

        if _carry:
            pre_node = ListNode(_carry)
            pre_node.next = node
            return pre_node

        return node


# stack
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        stack1 = []
        stack2 = []
        carry = 0

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            _sum = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10

            pre_next = dummy_head.next
            dummy_head.next = ListNode(_sum)
            dummy_head.next.next = pre_next

        return dummy_head.next


# dfs error record 錯誤紀錄
# 兩個node長度不一樣時 有問題
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         def dfs(n1,n2):
#             if not n1 and not n2:
#                 return None , 0
#             next_node = None
#             carry = 0

#             if n1.next and n2.next:
#                 next_node , carry = dfs(n1.next,n2.next)
#             elif n1.next:
#                 next_node , carry = dfs(n1.next,n2)
#             elif n2.next:
#                 next_node , carry = dfs(n1,n2.next)
#             v1 = n1.val if n1 else 0
#             v2 = n2.val if n2 else 0
#             _sum = (v1 + v2 + carry)%10
#             carry = (v1 + v2 + carry)//10
#             node = ListNode(_sum)
#             node.next = next_node
#             # n1 , n2 = None , None
#             return node , carry

#         node , _carry = dfs(l1,l2)

#         if _carry:
#             pre_node = ListNode(_carry)
#             pre_node.next = node
#             return pre_node

#         return  node not work

# @lc code=end
