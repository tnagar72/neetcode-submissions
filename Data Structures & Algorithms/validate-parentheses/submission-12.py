class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        self.dict = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in self.dict.values():
                self.stack.append(char)
                continue
            if char in self.dict:
                if len(self.stack) == 0:
                    return False
                if self.dict[char] == self.stack.pop():
                    continue
                else:
                    return False
                    
        if len(self.stack) != 0:
            return False
        else:
            return True