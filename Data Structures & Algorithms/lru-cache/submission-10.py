class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.first_node, self.last_node = Node(None, None), Node(None, None)
        self.first_node.nxt, self.last_node.prev = self.last_node, self.first_node
        
    def remove(self, node):
        prev_node, next_node = node.prev, node.nxt
        prev_node.nxt, next_node.prev = next_node, prev_node
        return None
    def insert(self, node):
        """
        Will insert node as the last node in the doubly linked list, right before the 'last_node' dummy node
        """
        actual_last_node = self.last_node.prev
        actual_last_node.nxt = node
        node.prev = actual_last_node
        self.last_node.prev = node
        node.nxt = self.last_node
        return None

    def get(self, key: int) -> int:
        if key in self.cache:
            curr_node = self.cache[key]
            return_val = self.cache[key].value
            self.remove(curr_node)
            self.insert(curr_node)
            return return_val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update value of key and also reposition node associated with the key
            # OR remove node and add a new node with new value to the end and reassign this node's address to the hashmap cache
            curr_node = self.cache[key]
            self.remove(curr_node)
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
        else:
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                lru_node = self.first_node.nxt
                self.remove(lru_node)
                lru_key = lru_node.key
                del self.cache[lru_key]
        return None
        
