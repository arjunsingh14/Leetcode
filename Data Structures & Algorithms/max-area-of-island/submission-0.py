class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if (
                min(r, c) < 0
                or r == ROW or c == COL
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))

            return dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1) + 1
        maxIsland = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxIsland = max(maxIsland, dfs(r, c))
        return maxIsland