class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        
        newString = ""

        while l < len(word1) and l < len(word2):
            newString += f"{word1[l]}{word2[l]}"
            l += 1
        
        newString += word2[l:]
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