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