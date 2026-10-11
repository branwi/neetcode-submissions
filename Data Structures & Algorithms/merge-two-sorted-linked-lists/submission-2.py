# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        tail = head
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            tail.next = ListNode(None)
            tail = tail.next
            if curr1.val < curr2.val:
                tail.val = curr1.val
                curr1 = curr1.next
            else:
                tail.val = curr2.val
                curr2 = curr2.next
        if curr2:
            while curr2:
                tail.next = ListNode(None)
                tail = tail.next
                tail.val = curr2.val
                curr2 = curr2.next
        if curr1:
            while curr1:
                tail.next = ListNode(None)
                tail = tail.next
                tail.val = curr1.val
                curr1 = curr1.next
        return head.next