class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0], 0, 0]]
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        heapq.heapify(minHeap)
        visit = set((0, 0))
        maxTime = 0
        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            if r == ROW - 1 and c == COL - 1:
                return w
            for dr, dc in direct:
                neiR, neiC = r + dr, c + dc
                if (
                    min(neiR, neiC) < 0
                    or neiR == ROW or neiC == COL
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(w, grid[neiR][neiC]), neiR, neiC])
            

            

        