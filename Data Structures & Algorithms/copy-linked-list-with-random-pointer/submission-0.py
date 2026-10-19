"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None:None}
        curr = head
        while curr:
            val = curr.val
            newNode = Node(val)
            nodeToCopy[curr] = newNode
            curr = curr.next
        curr = head

        while curr:
            newNode = nodeToCopy[curr]
            newNode.next = nodeToCopy[curr.next]
            newNode.random = nodeToCopy[curr.random]
            curr = curr.next

        return nodeToCopy[head]
        