class DynamicArray:
    
    def __init__(self, capacity: int):
       self.capacity = capacity
       self.size = 0
       self.initarr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.initarr[i]

    def set(self, i: int, n: int) -> None:
        self.initarr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.initarr[self.size] = n 
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.initarr[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] *  self.capacity
        for i in range(self.size):
            new_arr[i] = self.initarr[i]
        self.initarr = new_arr

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
