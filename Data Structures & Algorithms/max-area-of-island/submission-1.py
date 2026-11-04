class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
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
            other_islands = 0
            for dr, dc in direct:
                other_islands += dfs(r + dr, c + dc)
            
            return 1 + other_islands
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, dfs(r, c))
        return max_area