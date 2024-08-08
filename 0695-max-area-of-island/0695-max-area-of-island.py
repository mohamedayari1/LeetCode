from typing import List
import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        raws, cols = len(grid), len(grid[0])

        max_area = 0 

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            current_area = 1  
            
            while queue:
                raw, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = raw + dr, col + dc
                    if (
                        nr in range(raws) and 
                        nc in range(cols) and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        current_area += 1
            return current_area
                    

        for r in range(raws):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r, c))  
                    max_area = max(max_area, bfs(r, c))
        return max_area
