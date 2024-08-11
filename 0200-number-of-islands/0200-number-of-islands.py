class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def helper(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = collections.deque([(r, c)])
            visited.add((r, c))

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (nr in range(ROWS) and 
                            nc in range(COLS) and 
                            (nr, nc) not in visited and 
                            grid[nr][nc] == "1"):

                            visited.add((nr, nc))
                            queue.append((nr, nc))

        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    helper(r, c)
                    result += 1
        return result