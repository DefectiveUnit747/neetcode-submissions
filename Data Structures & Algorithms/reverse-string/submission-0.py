class Solution:
    def reverseString(self, s: List[str]) -> None:
        midpoint = len(s) / 2
        l = 0
        while l < midpoint:
            secondIndex = (len(s) -1) - l
            temp = s[l]
            s[l] = s[secondIndex]
            s[secondIndex] = temp
            l += 1

 
"""

[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
len = 7
0, 6
1, 5

"""
