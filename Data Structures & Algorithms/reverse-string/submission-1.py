class Solution:
    def reverseString(self, s: List[str]) -> None:
        midpoint = len(s) / 2
        l = 0
        while l < midpoint:
            secondIndex = (len(s) -1) - l
            s[l], s[secondIndex] = s[secondIndex], s[l]
            l += 1