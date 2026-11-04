class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        direct = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(r, c):
            if (
                min(r, c) < 0
                or r == ROW or c == COL
                or (r, c) in visit
                or grid[r][c] == "0"
            ):
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    count += 1
        return count
