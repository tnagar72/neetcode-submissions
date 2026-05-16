class HashTable:
    
    class Pair():
        def __init__(self, key, val, next_pair = None):            
            self.key = key
            self.val = val
            self.next_pair = next_pair
    
    def __init__(self, capacity: int):
        if capacity <= 1:
            raise NotImplementedError("<= 1")
        self.size = 0
        self.capacity = capacity
        self.map = []
        for i in range(self.capacity):
            self.map.append(None)



    def insert(self, key: int, value: int) -> None:
        hash_index = self.hash(key)

        if self.map[hash_index] == None:
            self.map[hash_index] = self.Pair(key, value)
            self.size += 1
            if self.size/self.capacity >= 0.5:
                self.resize()
            return None

        current_pair = self.map[hash_index]
        while True:
            if current_pair.key == key:
                current_pair.val = value
                return None
            
            if current_pair.next_pair == None:
                current_pair.next_pair = self.Pair(key, value)
                self.size += 1
                if self.size/self.capacity >= 0.5:
                    self.resize()
                return None

            current_pair = current_pair.next_pair
        
        raise NotImplementedError("Kuch toh gadbad hai")
        return None


    def get(self, key: int) -> int:
        hash_index = self.hash(key)

        if self.map[hash_index] == None:
            return -1
        
        current_pair = self.map[hash_index]
        while True:
            if current_pair.key == key:
                return current_pair.val
            else:
                current_pair = current_pair.next_pair
            
            if current_pair == None:
                return -1
        
        return -1

    def remove(self, key: int) -> bool:
        hash_index = self.hash(key)

        if self.map[hash_index] == None:
            return False
        else:
            if self.map[hash_index].key == key:
                self.map[hash_index] = self.map[hash_index].next_pair
                self.size -= 1
                return True
            prev_pair = self.map[hash_index]
            current_pair = self.map[hash_index].next_pair
            while True:
                if current_pair == None:
                    return False
                
                if current_pair.key == key:
                    prev_pair.next_pair = current_pair.next_pair
                    self.size -= 1
                    return True

                prev_pair, current_pair = current_pair, current_pair.next_pair
    
        raise NotImplementedError("Should not reach here")
        return False


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return len(self.map)


    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        self.size = 0
        new_map = []
        for i in range(self.capacity):
            new_map.append(None)
        old_map = self.map
        self.map = new_map
        for element in old_map:
            if element == None:
                continue
            else:
                while True:
                    self.insert(element.key, element.val)
                    element = element.next_pair
                    if element == None:
                        break

    def hash(self, key):
        sum = 0
        for i in str(key):
            sum += ord(i)
        
        return sum % self.capacity ## unsure here


