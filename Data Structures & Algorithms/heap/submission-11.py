class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = tmp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and
            self.heap[2 * i + 1] < self.heap[i] and
            self.heap[2 * i + 1] < self.heap[2 * i]):
                tmp = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                tmp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = tmp
                i = 2 * i
            else:
                break
        return res
        

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return
        nums.append(nums[0])
        self.heap = nums
        curr = (len(self.heap) - 1) // 2
        while curr > 0:
            i = curr
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[i] and
                self.heap[2 * i + 1] < self.heap[2 * i]):
                    tmp = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i + 1
                elif self.heap[2 * i] < self.heap[i]:
                    tmp = self.heap[2 * i]
                    self.heap[2 * i] = self.heap[i]
                    self.heap[i] = tmp
                    i = 2 * i
                else:
                    break
            curr -= 1
            
        