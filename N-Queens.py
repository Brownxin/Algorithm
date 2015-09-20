class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        board=[-1 for i in range(n)]
        res=[]
        def check(row,column):
            for i in range(row):
                if board[i]==column or abs(i-row)==abs(board[i]-column):
                    return False
            return True
        def put_queue(row,list_temp):
            if row==n:
                res.append(list_temp)
            for i in range(n):
                if check(row,i):
                    board[row]=i
                    list=['.' for i in range(n)]
                    put_queue(row+1,list[:i]+'Q'+list[i+1:])

        put_queue(0,list)
        return res