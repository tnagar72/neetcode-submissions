class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        resultArray = [0] * len(temperatures)

        for index, element in enumerate(temperatures):
            if not stack:
                stack.append((element, index))
            elif element <= stack[-1][0]:
                    stack.append((element, index))
            else:

                while stack[-1][0] < element:
                    poppedValue = stack.pop()
                    resultArray[poppedValue[1]] =  index - poppedValue[1]

                    if not stack:
                        break

                stack.append((element, index)) 
        

        return resultArray


        