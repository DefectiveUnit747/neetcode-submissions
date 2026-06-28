class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        for word in strs:
            letters = "".join((sorted(word)))
            if letters in wordDict:
                wordDict[letters].append(word)
            else:
                wordDict[letters] = [word]

        return [value for key, value in wordDict.items()]