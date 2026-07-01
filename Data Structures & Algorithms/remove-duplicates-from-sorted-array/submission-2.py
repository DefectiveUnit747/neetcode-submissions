class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        length = len(nums) - 1
        
        while r <= length:
            current = nums[l]
            if nums[r] == current:
                nums.pop(r)
                length -= 1
            else:
                l += 1
                r = l + 1

        return len(nums)
