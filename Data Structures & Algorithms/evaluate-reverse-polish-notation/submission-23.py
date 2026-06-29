import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        valueStack = []
        for element in tokens:
            if element in operators:
                firstVal = valueStack.pop()
                secondVal = valueStack.pop()
                
                if element == "+":
                    result = int(firstVal) + int(secondVal)
                elif element == "*":
                    result = int(firstVal) * int(secondVal)
                elif element == "/":
                    result = int(secondVal) / int(firstVal)
                    result = (math.trunc(result))
                else:
                    result = int(secondVal) - int(firstVal)             
                valueStack.append(result)
            
            else:
                valueStack.append(element)

        return int(valueStack[0])