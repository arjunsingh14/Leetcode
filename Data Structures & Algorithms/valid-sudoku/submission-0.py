from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict, colDict, sqDict = defaultdict(set), defaultdict(set), defaultdict(set)
        ROW, COL = len(board), len(board[0])
        for r in range(ROW):
            for c in range(COL):
                elem = board[r][c]
                if elem == ".":
                    continue
                if (
                    elem in rowDict[r] or
                    elem in colDict[c] or
                    elem in sqDict[(r // 3, c // 3)]
                ):
                    return False
                rowDict[r].add(elem)
                colDict[c].add(elem)
                sqDict[(r // 3, c // 3)].add(elem)

        return True