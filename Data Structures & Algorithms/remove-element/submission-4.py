class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        length = len(nums)

        while r < length:
            if nums[l] == val: #Want this so can swap to the end
                if nums[r] != val: # If the r pointer is a diff value, want it to front
                    nums[l], nums[r] = nums[r], nums[l] #Swap them
                    l += 1 #l is not not a value, so increment
            else:
                l += 1
            r += 1

        return l

#Want everything NOT target to the front
