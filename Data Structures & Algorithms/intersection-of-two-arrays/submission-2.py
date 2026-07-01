class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        totalSet = []

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        l1 = len(nums1)
        l2 = len(nums2)

        l, r = 0, 0

        while (l < l1) and (r < l2):
            if nums1[l] > nums2[r]:
                r += 1
            elif nums1[l] == nums2[r]:
                if nums1[l] not in totalSet:
                    totalSet.append(nums1[l])
                l += 1
                r += 1
            else:
                l += 1
        
        return totalSet