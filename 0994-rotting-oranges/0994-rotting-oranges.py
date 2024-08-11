class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_ones = 0
        queue = collections.deque()
        visited = set()
        tracker = set()

        for r in range(ROWS):
            for c in range(COLS):
                tracker.add(grid[r][c])
                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_ones += 1

        if 2 not in tracker:
            if 1 in tracker:
                return -1
            else:
                return 0
        
        result = -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                visited.add((row, col))

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and 
                        (nr, nc) not in visited):
                        
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_ones -= 1
                            queue.append((nr, nc))
            result += 1

        if fresh_ones > 0:
            return -1

        else:
            return result


