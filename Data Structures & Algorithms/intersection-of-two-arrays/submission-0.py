class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        total = []
        for element in  nums1:
            if element in nums2 and element not in total:
                total.append(element)

        return total