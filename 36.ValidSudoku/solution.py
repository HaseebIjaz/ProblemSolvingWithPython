class Solution:
    def isValidSudoku(self, board:List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": return
                num = board[r][c]
                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[(r//3,c//3)]):
                    return False
        return True