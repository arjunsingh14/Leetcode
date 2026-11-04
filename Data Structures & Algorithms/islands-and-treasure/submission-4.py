class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        direct = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r, c])
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    n_row, n_col = r + dr, c + dc
                    if (
                        min(n_row, n_col) < 0
                        or n_row == ROW
                        or n_col == COL
                        or grid[n_row][n_col] != INF
                    ):
                        continue
                    q.append([n_row, n_col])
                    grid[n_row][n_col] = dist
            dist += 1
        
