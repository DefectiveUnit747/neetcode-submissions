class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            midpoint = (r + l) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
        return -1
