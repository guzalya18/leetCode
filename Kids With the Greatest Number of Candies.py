
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        can = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                can.append(True)
            else:
                can.append(False)
        return can