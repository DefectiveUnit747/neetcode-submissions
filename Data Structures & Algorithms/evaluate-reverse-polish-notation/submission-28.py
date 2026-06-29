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
                    result = firstVal + secondVal
                elif element == "*":
                    result = firstVal * secondVal
                elif element == "/":
                    result = secondVal / firstVal
                    result = (math.trunc(result))
                else:
                    result = secondVal - firstVal      
                valueStack.append(result)
            else:
                valueStack.append(int(element))

        return valueStack[0]