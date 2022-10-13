# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = dummy = ListNode(-1,head)
        while head:
            if head.val != val:
                cur = head
            else:
                cur.next = head.next
            head = head.next
        return dummy.next
