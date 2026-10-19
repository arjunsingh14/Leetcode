# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        buffer = head
        for i in range(n):
            buffer = buffer.next
        curr = dummy
        while buffer:
            curr = curr.next
            buffer = buffer.next
        curr.next = curr.next.next
        return dummy.next