# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_lists(self, l1, l2):
        dummy = head = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next 

            head = head.next 
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next 

    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        res = lists[0]
        for i, curr in enumerate(lists[1:]):
            res = self.merge_two_lists(res, curr)
        return res 
            

        