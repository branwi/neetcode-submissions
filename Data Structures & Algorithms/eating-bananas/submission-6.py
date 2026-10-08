class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k: int):
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            return total

        l = 1
        r = max(piles)

        while l < r:
            curr = (l + r) // 2
            time_taken = hours(curr)

            if time_taken > h:
                l = curr + 1
            else:
                r = curr

        return r