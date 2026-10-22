class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacSet, atlSet = set(), set()
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, ocean, prevHeight):
            if (
                min(r, c) < 0
                or r == ROW or c == COL
                or (r, c) in ocean
                or heights[r][c] < prevHeight
            ):
                return
            ocean.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc, ocean, heights[r][c])
        
        for r in range(ROW):
            dfs(r, 0, pacSet, 0)
            dfs(r, COL - 1, atlSet, 0)
        for c in range(COL):
            dfs(0, c, pacSet, 0)
            dfs(ROW -1, c, atlSet, 0)
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in atlSet and (r, c) in pacSet:
                    res.append([r, c])
        return res
