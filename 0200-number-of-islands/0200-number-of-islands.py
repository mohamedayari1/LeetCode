class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        queue = collections.deque()

        def bfs(r, c):
            queue.append((r, c))
            seen.add((r, c))
            directions =[[1, 0], [-1, 0], [0, 1], [0, -1]]
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (nr in range(ROWS) and 
                            nc in range(COLS) and 
                            grid[nr][nc] == '1' and 
                            (nr, nc) not in seen):

                            queue.append((nr, nc))
                            seen.add((nr, nc))

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    result += 1
        return result 