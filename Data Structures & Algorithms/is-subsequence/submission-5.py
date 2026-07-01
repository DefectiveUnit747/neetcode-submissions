class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        currentLength = 0

        if s == "":
            return True
        
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
                currentLength += 1
                l += 1
                if currentLength == len(s):
                    return True

            r += 1
        print(currentLength)
        
        return False