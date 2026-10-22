class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if (
                min(r, c) < 0
                or r == ROW or c == COL
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    count += 1
        return count           

