class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictOfNum = {}
        for num in nums:
            dictOfNum[num] = target - num

        for num in range(0, len(nums)):
            targetToHit = dictOfNum[nums[num]]
            if targetToHit in nums and nums.index(targetToHit) != num:
                return sorted([num, nums.index(targetToHit)])