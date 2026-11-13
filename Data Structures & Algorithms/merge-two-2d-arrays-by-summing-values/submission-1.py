class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        combined = nums1 + nums2
        combined.sort(key=lambda x: x[0])
        sol = []
        for i in range(len(combined)):
            if i < len(combined) - 1 and combined[i][0] == combined[i + 1][0]:
                sol.append([combined[i][0], combined[i][1] + combined[i + 1][1]])
            elif i > 0 and combined[i][0] == combined[i-1][0]:
                continue
            else:
                sol.append(combined[i])

        return sol

