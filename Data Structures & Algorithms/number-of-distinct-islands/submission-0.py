class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROW or c == COL or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return
            visit.add((r, c))
            uniqueIsland.add((r - r0, c - c0))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        distinctIslands = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visit:
                    uniqueIsland = set()
                    r0, c0 = r, c
                    dfs(r, c)
                    if uniqueIsland:
                        distinctIslands.add(frozenset(uniqueIsland))
        return len(distinctIslands)
