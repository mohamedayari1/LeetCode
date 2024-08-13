class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_height):
            if (r not in range(ROWS) or 
                c not in range(COLS) or
                (r, c) in visited or
                heights[r][c] < prev_height):
                return
            visited.add((r, c))
            prev_height = heights[r][c]

            dfs(r+1, c, visited, prev_height)
            dfs(r-1, c, visited, prev_height)
            dfs(r, c+1, visited, prev_height)
            dfs(r, c-1, visited, prev_height)

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])


        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append((r, c))
        return result