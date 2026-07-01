class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums) - 1

        l, r = 0, 1

        while r <= length:
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l] = nums[r]
                    nums[r] = 0
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1
        print(nums)

        """
        Do not return anything, modify nums in-place instead.
        """
        