class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        def dfs(r, c):
            if (
                min(r, c) < 0
                or r == ROW or c == COL
                or board[r][c] != 'O'
                or (r, c) in visit
            ):
                return
            board[r][c] = 'T'
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        
        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL - 1)
        
        for c in range(COL):
            dfs(0, c)
            dfs(ROW - 1, c)
    
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
