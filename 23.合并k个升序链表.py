#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(lis1, lis2):
            if not lis1 or not lis2:
                return lis1 if lis1 else lis2
            dummy = ListNode()
            cur = dummy
            a, b = lis1, lis2
            while a and b:
                if a.val < b.val:
                    cur.next = a
                    a = a.next
                else:
                    cur.next = b
                    b = b.next
                cur = cur.next
            cur.next = a if a else b
            return dummy.next

        def btrack(lists, left, right):
            if left == right:
                return lists[left]
            if left > right:
                return None
            mid = (left+right)//2
            return merge(btrack(lists, left, mid), btrack(lists, mid+1, right))

        return btrack(lists, 0, len(lists)-1)
# @lc code=end
