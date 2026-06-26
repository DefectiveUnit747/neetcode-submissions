class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) >= len(t):
            sDict = self.makeDictionaryOfLetters(s)
            tDict = self.makeDictionaryOfLetters(t)
        else:
            tDict = self.makeDictionaryOfLetters(s)
            sDict = self.makeDictionaryOfLetters(t)
        for key, value in sDict.items():
            if key not in tDict:
                return False
            else:
                if value != tDict[key]:
                    return False
        return True

        
    def makeDictionaryOfLetters(self, word):
        dictOfLetters = {}
        for letter in word:
            if letter not in dictOfLetters:
                dictOfLetters[letter] = 1
            else:
                dictOfLetters[letter] += 1
        return dictOfLetters