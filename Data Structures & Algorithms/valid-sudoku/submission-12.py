class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for r in range(9):
            for c in range(9):
                square = (r // 3, c // 3)
                val = board[r][c]

                if val == '.':
                    continue
                if r not in row:
                    row[r] = set()
                if c not in col:
                    col[c] = set()
                if square not in box:
                    box[square] = set()

                if val not in row[r] and val not in col[c] and val not in box[square]:
                    row[r].add(val)
                    col[c].add(val)
                    box[square].add(val)
                else:
                    return False

        return True


                
                