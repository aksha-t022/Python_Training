class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def isSafe(row, col, digit):
            for ind in range(0, 9):
                if board[row][ind] == digit:
                    return False
            for ind in range(0, 9):
                if board[ind][col] == digit:
                    return False

            StartRow = (row // 3) * 3
            StartCol = (col // 3) * 3

            for r in range(StartRow, StartRow + 3):
                for t in range(StartCol, StartCol + 3):
                    if board[r][t] == digit:
                        return False
            return True

        def helperFunction(board, row, col):
            if row == 9:
                return True

            if col == 9:
                return helperFunction(board, row + 1, 0)

            if board[row][col] != '.':
                return helperFunction(board, row, col + 1)

            for digit in "123456789":
                if isSafe(row, col, digit):
                    board[row][col] = digit
                    if helperFunction(board, row, col + 1):
                        return True
                    board[row][col] = '.'

            return False

        helperFunction(board, 0, 0)