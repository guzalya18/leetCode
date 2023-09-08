class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        tg = 0
        for i in hours:
            if i >= target:
                tg += 1
        return tg