class Solution:
    def isPalindrome(self, s: str) -> bool:
        charsToRemove = []
        for letter in s:
            if not letter.isalpha() and not letter.isdigit():
                charsToRemove.append(letter)
        print(charsToRemove)
        for character in charsToRemove:
            s = s.replace(character, "")
        s = s.lower()

        length = len(s)
        
        frontPointer = 0
        endPointer = length - 1

        middleIndex = (length // 2) - 1
        while frontPointer <= middleIndex and endPointer >= middleIndex:
            if s[frontPointer] != s[endPointer]:
                return False
            frontPointer += 1
            endPointer -= 1
        return True
        

