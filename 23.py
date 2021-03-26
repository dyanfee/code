class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):

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
        mid = (left+right)//2
        return merge(btrack(lists, left, mid), btrack(lists, mid+1, right))

    return btrack(lists, 0, len(lists)-1)


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
c = []
for i in lists:
    head = ListNode()
    cur = head
    for j in i:
        cur.next = ListNode(j)
        cur = cur.next
    c.append(head.next)
r = mergeKLists(c)
res = []
while r:
    res.append(r.val)
    r = r.next
print(res)
