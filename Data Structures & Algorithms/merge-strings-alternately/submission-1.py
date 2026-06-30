class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        if len(word1) < len(word2):
            r = len(word1)
            case = 1
        elif len(word1) == len(word2):
            r = len(word1)
            case = 2
        else:
            r = len(word2)
            case = 3

        newString = ""

        while l < r:
            newString += f"{word1[l]}{word2[l]}"
            l += 1
        
        if case == 1:
            newString += word2[l:]
        elif case == 3:
            newString += word1[l:]

        return newString
        
        
        
        
        
        
        
        
        
        
"""       
newString = ""
while word1 and word2:
    newString += word1[0]
    newString += word2[0]
    word1 = word1[1:]
    word2 = word2[1:]

if word1:
    newString += word1
if word2:
    newString += word2
return newString
"""