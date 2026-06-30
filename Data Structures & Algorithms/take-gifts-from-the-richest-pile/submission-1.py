import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxVal = 0
            index = 0
            for gift in gifts:
                if gift > maxVal:
                    maxVal = gift
                    index = gifts.index(gift)
                
            newMax = math.floor(math.sqrt(maxVal))
            gifts[index] = newMax

        sumG = 0
        for gift in gifts:
            sumG += gift
        return sumG