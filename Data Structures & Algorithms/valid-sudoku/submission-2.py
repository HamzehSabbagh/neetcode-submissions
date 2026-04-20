class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for r in range(9):
            for c in range(9):
                box = (r // 3, c // 3) # (0, 0)
                val = board[r][c] # 1
                if val == ".":
                    continue
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box not in squares:
                    squares[box] = set()

                if val in rows[r] or val in cols[c] or val in squares[box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[box].add(val)
        return True


                