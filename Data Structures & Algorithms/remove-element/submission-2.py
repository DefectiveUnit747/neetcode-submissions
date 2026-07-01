class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        length = len(nums)

        while r < length:
            if nums[l] == val:
                if nums[r] != val:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                r += 1
            else:
                l += 1
                r += 1
        print(nums)
        return l
"""
[2, 3, 2]
l = 1, r = 2
val = 2
[2, 2, 3]

"""