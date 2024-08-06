class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        raws, cols = len(grid), len(grid[0])
        visited = set()        
        nbr_islands = 0

        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = collections.deque([(r, c)])
            while queue:
                for _ in range(len(queue)):
                    raw, col = queue.popleft()
                    for dr, dc in directions:
                        r, c = raw + dr, col + dc

                        if (r in range(raws) and
                            c in range(cols) and 
                            (r, c) not in visited and
                            grid[r][c] == "1"  
                        ):
                            queue.append((r, c))
                            visited.add((r, c))


        for r in range(raws):
            for c in range(cols):
                if (grid[r][c] == "1" and 
                    (r, c) not in visited):
                    bfs(r, c)
                    nbr_islands += 1
        return nbr_islands    
                