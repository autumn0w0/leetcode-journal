class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        repeats = 0
        if nums != []: 
            for i in nums: 
                repeats ^= i 
            return repeats
            