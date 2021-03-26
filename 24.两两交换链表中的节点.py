#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = ListNode()
        res.next = head
        cur = res
        while cur.next and cur.next.next:
                pre = cur.next
                nex = cur.next.next
                cur.next = nex
                pre.next = nex.next
                nex.next = pre
                cur = pre
        return res.next
# @lc code=end
