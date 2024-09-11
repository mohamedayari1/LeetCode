class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS  = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visited.add((r, c))
            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc 

                        if (nr in range(ROWS) and
                            nc in range(COLS) and
                            grid[nr][nc] == "1" and
                            (nr, nc) not in visited):

                            queue.append((nr, nc))
                            visited.add((nr, nc))
        
        num_of_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_of_islands += 1
        return num_of_islands