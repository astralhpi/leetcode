class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if self.checkHead(board, i, j):
                    count += 1
        return count
    
    def checkHead(self, board, rowIdx, colIdx):
        result = board[rowIdx][colIdx] == 'X'
        result = result and (rowIdx == 0 or board[rowIdx-1][colIdx] != 'X')
        result = result and (colIdx == 0 or board[rowIdx][colIdx-1] != 'X')
        return result
