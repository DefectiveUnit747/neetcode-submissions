import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(0, k):
            gifts = sorted(gifts, reverse=True)
            gifts[0] = math.floor(math.sqrt(gifts[0]))


        return sum(gifts)