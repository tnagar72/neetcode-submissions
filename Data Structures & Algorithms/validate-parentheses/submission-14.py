class Solution:
    def isValid(self, s: str) -> bool:

        mp = {"}": "{", "]": "[", ")": "("}
        stack = []

        for bracket in s:
            if bracket in mp.keys():
                if len(stack) == 0:
                    return False
                else:
                    popped_element = stack.pop()
                    if mp[bracket] == popped_element:
                        continue
                    else:
                        return False
            else:
                stack.append(bracket)

        
        if not len(stack) == 0:
            return False
        else:
            return True

        