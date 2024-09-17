class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        def bfs(r, c):
            queue.append((r, c))
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (nr in range(ROWS) and 
                            nc in range(COLS) and
                            grid[nr][nc] == 1 and 
                            (nr, nc) not in visited):
                            
                            area += 1
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            
            return area 
        max_area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(bfs(r, c), max_area)
        return max_area 