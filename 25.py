class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        tail = dummy
        while head:
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverseList2(head, tail)
            # 链接回去
            tail.next = nex
            pre.next = head
            pre = tail
            head = tail.next
        return dummy.next

    def reverseList1(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList2(self, head, tail):
        pre = tail.next
        nex = head
        while pre != tail:
            tmp = nex.next
            nex.next = pre
            pre = nex
            nex = tmp
        return tail, head


lists = [1, 2, 3, 4, 5]
k = 2
head = ListNode()
cur = head
for j in lists:
    cur.next = ListNode(j)
    cur = cur.next
s = Solution()
r = s.reverseKGroup(head.next,k)
res = []
while r:
    res.append(r.val)
    r = r.next
print(res)
