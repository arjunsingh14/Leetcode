class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()
        self.arr[self.length] = n
        self.length += 1
        
    def popback(self) -> int:
        if self.length > 0:
            element = self.arr[self.length - 1]
            self.arr[self.length - 1] = 0
            self.length -= 1
            return element

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newArr = [0] * (self.capacity)
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity