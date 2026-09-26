class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        seen = set()
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                curr = nums[i] + nums[j]
                goal = target - curr

                while l < r:
                    total = nums[l] + nums[r]
                    if total == goal:
                        if (nums[i], nums[j], nums[l], nums[r]) not in seen:
                            sol.append([nums[i], nums[j], nums[l], nums[r]])
                            seen.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif total > goal:
                        r -= 1
                    else:
                        l += 1
        return sol

        