class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = right * min(heights[left], heights[right])
        while left < right:
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            
            width = right - left
            water = width * min(heights[left], heights[right])
            max_water = max(max_water, water)
        
        return max_water
            