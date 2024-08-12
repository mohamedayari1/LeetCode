class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                (r, c)  in visited or 
                heights[r][c] < prev_height):
                return

            visited.add((r, c))
            prev_height = heights[r][c]

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                dfs(nr, nc, visited, prev_height)
        
        for c in range(COLS):
            prev_height = heights[0][c]
            dfs(0, c, pacific, prev_height)

            prev_height = heights[ROWS - 1][c]
            dfs(ROWS - 1, c, atlantic, prev_height)

        for r in range(ROWS):
            prev_height = heights[r][0]
            dfs(r, 0, pacific, prev_height)

            prev_height = heights[r][COLS - 1]
            dfs(r, COLS - 1, atlantic, prev_height)

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result


        