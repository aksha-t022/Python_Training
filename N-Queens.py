class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        bod=[["."]*n for _ in range(n)]
        
        def isSafe(b,row,col):
            for i in range(row):
                if b[i][col] == 'Q':
                    return False
            i,j=row-1,col-1
            while i>=0 and j>=0:
                if b[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i,j=row-1,col+1
            while i>=0 and j<n:
                if b[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True

        def helperFunction(board,row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for col in range(n):
                if isSafe(board,row,col):
                    board[row][col] = 'Q'
                    helperFunction(board,row+1)
                    board[row][col] = '.'
        
        helperFunction(bod,0)
        return result