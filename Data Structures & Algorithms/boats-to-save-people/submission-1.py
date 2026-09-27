class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        total = 0
        
        while l <= r:
            weight = people[l] + people[r]

            if people[r] == limit:
                r -= 1
            elif weight > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            total += 1
        return total
        
