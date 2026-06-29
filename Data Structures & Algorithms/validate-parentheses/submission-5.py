class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(" : ")", 
                   "{" : "}", 
                   "[" : "]"}

        if len(s) % 2 != 0:
            return False
        
        stack = []
        for element in s:
            if element in mapping: #Open bracket
                stack.append(element)
            else: #Closed brackets
                if len(stack) > 0:
                    lastAdded = stack.pop()
                    if mapping[lastAdded] != element:
                        return False
                else:
                    return False
        

        return True if not stack else False