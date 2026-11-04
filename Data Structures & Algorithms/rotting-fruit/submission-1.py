class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        direct = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        q = deque()
        visit = set()
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    count += 1
        time = 0
        while count and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    n_row, n_col = r + dr, c + dc
                    if (
                        min(n_row, n_col) < 0
                        or n_row == ROW
                        or n_col == COL
                        or grid[n_row][n_col] != 1
                    ):
                        continue
                    q.append([n_row, n_col])
                    grid[n_row][n_col] = 2
                    count -= 1
            time += 1
        return time if not count else -1