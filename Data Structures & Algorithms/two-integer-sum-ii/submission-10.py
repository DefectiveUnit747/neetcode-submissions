class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1

        while r > 0:
            for index in range(0, r):
                if numbers[index] + numbers[r] == target:
                    return [index + 1, r + 1]
            r -= 1