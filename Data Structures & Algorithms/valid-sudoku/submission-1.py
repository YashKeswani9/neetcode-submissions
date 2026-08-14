class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boards = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r] or 
                        board[r][c] in columns[c] or
                        board[r][c] in boards[r//3, c//3]):
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boards[r//3,c//3].add(board[r][c])
        
        return True