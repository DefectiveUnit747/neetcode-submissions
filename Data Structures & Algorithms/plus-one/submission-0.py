class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        total = 0
        for index in range(0, len(digits)):
            total += (digits[index] * (10**(length - (index+1))))

        total += 1
        return [int(i) for i in str(total)]