class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        if (capacity <= 0):
            raise Exception("Capacity must be positive")
        self.length = 0
        # Initialize a new array
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        # We are assuming index i is valid
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        # We know that length is number of elements in array so to get to the next empty space, index will be length itself cuze 0-indexing
        self.arr[self.length] = n
        self.length = self.length + 1
        return None

    def popback(self) -> int:
        return_val = self.arr[self.length - 1]
        self.length -= 1
        return return_val

    def resize(self) -> None:
        new_capacity = 2 * self.capacity
        new_arr = [0] * new_capacity
        # copy all elements over
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        # All elements copied over so we preserve new array qualities
        self.arr = new_arr
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity