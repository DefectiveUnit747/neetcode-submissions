class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r =  1, 1

        length = len(nums) - 1

        while r <= length:
            #check If l value is a unique one
            if nums[r] != nums[l - 1]:
                #unique value
                nums[l] = nums[r]
                l += 1
     
            r += 1
        return l
