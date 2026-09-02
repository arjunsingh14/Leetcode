from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visit = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dist = 0
        while q:
            dist += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direct:
                    row, col = r + dr, c + dc
                    if (
                        min(row, col) < 0 or
                        row == ROW or
                        col == COL or
                        (row, col) in visit or
                        grid[row][col] == - 1
                    ):
                        continue
                    visit.add((row, col))
                    grid[row][col] = dist
                    q.append([row, col])



            