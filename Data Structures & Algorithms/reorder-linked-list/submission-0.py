# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
    
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr1, curr2 = head, prev

        while curr2:
            nxt1, nxt2 = curr1.next, curr2.next
            curr1.next, curr2.next = curr2, nxt1
            curr1, curr2 = nxt1, nxt2