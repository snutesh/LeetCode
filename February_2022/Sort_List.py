# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        if head is None:
            return head
        while head != None:
            lst.append(head.val)
            head = head.next
        lst.sort()
        lst2 = ListNode()
        lst2.val = lst[0]
        temp = lst2
        for i in range(1, len(lst)):
            temp1 = ListNode()
            temp1.val = lst[i]
            temp.next = temp1
            temp = temp.next
        return lst2