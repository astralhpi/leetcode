class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(0, 9):
            for func in [self.posInRow, self.posInColumn, self.posInBox]:
                if self.hasDuplicate(board, func(i)):
                    return False
        return True
    
    def posInRow(self, rowIdx):
        for i in xrange(0, 9):
            yield (rowIdx, i)
    
    def posInColumn(self, colIdx):
        for i in xrange(0, 9):
            yield (i, colIdx)
    
    def posInBox(self, boxIdx):
        for i in xrange(0, 9):
            y = (boxIdx / 3) * 3 + (i / 3)
            x = (boxIdx % 3) * 3 + (i % 3)
            yield (y, x)
    
    def hasDuplicate(self, board, positions):
        appeared = set()
        for i, j in positions:
            value = board[i][j]
            if value != '.' and value in appeared:
                return True
            appeared.add(value)
            
        
        
        
