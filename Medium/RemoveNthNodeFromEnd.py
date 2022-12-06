# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offset = head
        dummy = cur = ListNode(0,head) 
        for i in range (n):
            offset = offset.next
        
        while offset:
            offset = offset.next
            cur = cur.next

        cur.next = cur.next.next

        return dummy.next
