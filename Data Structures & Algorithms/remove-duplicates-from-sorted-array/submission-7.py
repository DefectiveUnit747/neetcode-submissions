class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r =  1, 1

        length = len(nums)

        if length <= 1:
            return l

        while r < length:
            if nums[r] != nums[l - 1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
