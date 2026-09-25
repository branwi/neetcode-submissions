class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        walls = []
        total = 0
        if height[0] > height[1]:
            walls.append(0)

        for i in range(1, len(height) - 1):
            if (height[i-1] <= height[i] and height[i] > height[i+1]) or (height[i-1] < height[i] and height[i] >= height[i+1]):
                walls.append(i)
        
        if height[-1] > height[-2]:
            walls.append(len(height) - 1)
        
        l = 0
        r = 1
        while r < len(walls):
            left_wall = height[walls[l]]
            best_r = r
            for k in range(r, len(walls)):
                if height[walls[k]] > height[walls[best_r]]:
                    best_r = k
                if height[walls[best_r]] >= left_wall:
                    break
            r = best_r
            right_wall = height[walls[r]]

            min_h = min(left_wall, right_wall)
            print(min_h)
            for j in range(walls[l] + 1, walls[r]):
                water = min_h - height[j]
                if water > 0: total += water
                
            l = r
            r += 1
        
        return total


        