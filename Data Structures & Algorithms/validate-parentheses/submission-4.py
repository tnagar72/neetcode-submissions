class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        self.dict1 = {
            "[": "]",
            "(": ")",
            "{": "}",
        }

        for char in s:
            if char in self.dict1.keys():
                self.stack.append(char)
                continue
            if char in self.dict1.values():
                if len(self.stack) == 0:
                    return False
                if self.dict1[self.stack.pop()] == char:
                    continue
                else:
                    return False

        if len(self.stack) != 0:
            return False
        return True

               