# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create sentinel node - points to beginning of output list
        # while loop:
        # point sentinel.next to whichever is smallest between the two list heads
        # set head of that list to the next node
        # set cur pointer to sentinel.next
        # repeat until no more nodes left in either list
        # since the rest of the remaining list is sorted, point sentinel.next to it

        sentinel = ListNode()
        tail = sentinel

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 and not list2:
            tail.next = list1
        elif list2 and not list1:
            tail.next = list2

        return sentinel.next
            