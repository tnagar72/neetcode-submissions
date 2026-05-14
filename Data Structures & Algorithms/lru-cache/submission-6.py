class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.cache[key][1] = self.count
            self.count += 1
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key][1] = self.count
            self.count += 1
            self.cache[key][0] = value
        else:
            # key not in cache so needs to be added
            if not (len(self.cache.keys()) >= self.capacity):
                #  cache not full so key can just be added
                self.cache[key] = [value, self.count]
                self.count += 1
            else:
                # cache is full so LRU element needs to be pulled out
                cache_access_pattern = [(key, self.cache[key][1]) for key in self.cache.keys()]
                cache_access_pattern.sort(key = lambda x: x[1])
                self.cache.pop(cache_access_pattern[0][0])
                # Now that LRU element is removed we can add the key key-value pair
                self.cache[key] = [value, self.count]
                self.count += 1
        return None


