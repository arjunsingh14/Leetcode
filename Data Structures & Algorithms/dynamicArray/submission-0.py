class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        if i < self.length:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            val = self.array[self.length - 1]
            self.length -= 1
            return val
            

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [0] * self.capacity
        for i in range(self.length):
            newArray[i] = self.array[i]
        self.array = newArray

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity