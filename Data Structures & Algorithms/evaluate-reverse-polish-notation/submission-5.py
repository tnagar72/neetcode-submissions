class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for idx, element in enumerate(tokens):
            val = element
            if val == "+":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value2 + value1)
            elif val == "-":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value2 - value1)
            elif val == "*":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value2 * value1)
            elif val == "/":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(int(value2/value1))
            else:
                stack.append(int(val))
        
        return stack.pop()



        