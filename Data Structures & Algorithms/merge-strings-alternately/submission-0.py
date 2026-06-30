class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
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