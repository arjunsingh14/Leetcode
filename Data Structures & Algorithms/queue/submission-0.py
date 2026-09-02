class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class Deque:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def isEmpty(self): 
        return self.head.next == self.tail
    
    def append(self, value):
        last_node = self.tail.prev
        new_node = ListNode(value)

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    
    def appendleft(self, value):
        first_node = self.head.next
        new_node = ListNode(value)

        new_node.prev = self.head
        new_node.next = first_node
        self.head.next = new_node
        first_node.prev = new_node
    
    def pop(self):
        if self.isEmpty():
            return -1
        new_last = self.tail.prev.prev
        pop_val = self.tail.prev.val

        new_last.next = self.tail
        self.tail.prev = new_last
        return pop_val
    
    def popleft(self):
        if self.isEmpty():
            return -1
        pop_val = self.head.next.val
        new_first = self.head.next.next
        self.head.next = new_first
        new_first.prev = self.head
        return pop_val


        
