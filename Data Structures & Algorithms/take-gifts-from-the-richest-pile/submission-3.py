import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            index = 0
            for gift in gifts:
                if gift > gifts[index]:
                    index = gifts.index(gift)
                
            gifts[index] = math.trunc(math.sqrt(gifts[index]))


        return sum(gifts)