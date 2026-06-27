class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbersDict = {}
        for number in nums:
            if number in numbersDict:
                numbersDict[number] += 1
            else:
                numbersDict[number] = 1
        for key, value in numbersDict.items():
            if value == 1:
                return key