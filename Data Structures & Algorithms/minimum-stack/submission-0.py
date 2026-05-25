class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_max = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.prefix_max.append(val)
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.prefix_max.append(min(self.prefix_max[-1], val))

    def pop(self) -> None:
        return_val = self.stack.pop()
        self.prefix_max.pop()
        return return_val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix_max[-1]
        
