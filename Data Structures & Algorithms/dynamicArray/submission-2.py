class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() >= self.getCapacity():
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            element = self.array[self.length - 1]
            self.array[self.length - 1] = 0
            self.length -= 1
            return element

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [0] * self.capacity
        for i in range(len(self.array)):
            newArray[i] = self.array[i]
        self.array = newArray

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity