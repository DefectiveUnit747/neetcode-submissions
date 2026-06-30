class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majNumber = len(nums) // 2
        hashmap = {}
        for number in nums:
            if number in hashmap:
                hashmap[number] += 1
            else:
                hashmap[number] = 1
        
        
        for key, value in hashmap.items():
            if value >= majNumber:
                return key
        
        
        
        
        
        
        