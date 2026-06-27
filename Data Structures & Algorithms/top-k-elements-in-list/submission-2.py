class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbersDict = {}
        for number in nums:
            if number not in numbersDict:
                numbersDict[number] = 1
            else:
                numbersDict[number] += 1
        currentMaxOccurences = 0

        maxValues = []

        for key, value in numbersDict.items():
            maxValues.append([key, value])

        maxValues = sorted(maxValues, key = lambda x: x[1], reverse = True)
        print(maxValues)
        finalVals = []
        for i in range(0, k):
            finalVals.append(maxValues[i][0])
        return finalVals
                
                


