class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            if num in res:
                return num
            else:
                res.add(num)