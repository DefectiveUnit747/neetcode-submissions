class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(0, len(nums)):
            for secondNum in range(0, len(nums)):
                if num != secondNum:
                    total = nums[num] + nums[secondNum]
                    if total == target:
                        indices = sorted([num, secondNum])
        return indices