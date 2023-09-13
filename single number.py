class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for elem in set(nums):
            if nums.count(elem)==1:
                return elem