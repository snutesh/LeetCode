# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1
        if not n or not k % n:
            return head
        tail = head
        for x in range(n - k % n - 1):
            tail = tail.next
        next, tail.next, pre.next = tail.next, None, head
        return next