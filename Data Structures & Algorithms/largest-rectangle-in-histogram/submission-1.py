class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = [0]
        stack = [] #height, first
        heights.append(0)
        for i in range(len(heights)):
            first_position = i
            while stack and heights[i] < stack[-1][0]:
                first_position = stack[-1][1]
                area.append(stack[-1][0] * (i - stack[-1][1]))
                stack.pop()
            stack.append([heights[i], first_position])
        
        return max(area)
            