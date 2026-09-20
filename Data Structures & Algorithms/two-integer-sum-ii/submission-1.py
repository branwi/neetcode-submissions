class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1

        while a < b:
            total = numbers[a] + numbers[b]
            if total == target:
                return [a + 1, b + 1]
            elif total < target:
                a += 1
            else:
                b -= 1
        
        return []
        