# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = dummy = ListNode()
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tmp.next = curr1
                curr1 = curr1.next
            else:
                tmp.next = curr2
                curr2 = curr2.next
            
            tmp = tmp.next


        if not curr1:
            tmp.next = curr2
        if not curr2:
            tmp.next = curr1
        
        return dummy.next