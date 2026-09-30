class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #height, first
        heights.append(0)
        for i in range(len(heights)):
            first_position = i
            while stack and heights[i] < stack[-1][0]:
                first_position = stack[-1][1]
                maxArea = max(maxArea, stack[-1][0] * (i - stack[-1][1]))
                stack.pop()
            stack.append([heights[i], first_position])
        
        return maxArea
            