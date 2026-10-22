class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    count += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        minutes = 0
        while count and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr == ROW or c + dc == COL
                        or grid[r + dr][c + dc] in [2, 0]
                    ):
                        continue
                    count -= 1
                    grid[r + dr][c + dc] = 2
                    q.append([r + dr, c + dc])
            minutes += 1
        return minutes if not count else -1