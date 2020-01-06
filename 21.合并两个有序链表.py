#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            ret = l2
            ret.next = self.mergeTwoLists(l1, l2.next)
        else:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        return ret
# @lc code=end
