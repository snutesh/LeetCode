# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = []
        if list1 is None and list2 is None:
            return 
        while list1!=None:
            list3.append(list1.val)
            list1 = list1.next
        while list2!=None:
            list3.append(list2.val)
            list2 = list2.next
        list3.sort()
        lst2 = ListNode()
        lst2.val = list3[0]
        temp = lst2
        for i in range(1, len(list3)):
            temp1 = ListNode()
            temp1.val = list3[i]
            temp.next = temp1
            temp = temp.next
        return lst2