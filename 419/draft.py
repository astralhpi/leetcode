class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'X':
                    count += 1
                    
                    colIdx = j+1
                    rowIdx = i+1
                    while colIdx < len(board[i]) and board[i][colIdx] == 'X':
                        board[i][colIdx] = '.'
                        colIdx += 1
                    while rowIdx < len(board) and board[rowIdx][j] == 'X':
                        board[rowIdx][j] = '.'
                        rowIdx += 1
        return count
                
                
        
