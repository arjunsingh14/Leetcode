class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        if grid[ROW - 1][COL - 1] == 1 or grid[0][0] == 1:
            return -1
        visit = set((0, 0))
        q = deque([[0, 0]])
        length = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length
                for dr, dc in direct:
                    if (min(r + dr, c + dc) < 0
                    or r + dr == ROW or c + dc == COL
                    or (r + dr, c + dc) in visit
                    or grid[r + dr][c + dc] == 1
                    ):
                        continue
                    visit.add((r + dr, c + dc))
                    q.append([r + dr, c + dc])
            length += 1
        return -1
