class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        c = image[sr][sc]
        visited = set()
        image[sr][sc] = color
        def get_neighbors(coords):
            directions = [
                [0, 1], [0, -1], [1, 0], [-1, 0]
            ]
            x, y = coords
            valid_neighbors = []
            for d in directions:
                cx, cy = d
                new_x = x + cx
                new_y = y + cy
                if (new_x < m and new_x >= 0 and new_y < n and new_y >= 0 and (new_x, new_y) not in visited):
                    if image[new_x][new_y] == c:
                        image[new_x][new_y] = color
                        valid_neighbors.append([new_x, new_y])
                        visited.add((new_x, new_y))
            return valid_neighbors

        stack = [[sr, sc]]
        while stack:
            coord = stack.pop()
            for neighbor in get_neighbors(coord):
                stack.append(neighbor)
        
        return image
