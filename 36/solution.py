class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for func in [self.posInRow, self.posInColumn, self.posInBox]:
            for i in xrange(0, 9):
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
            row = (boxIdx / 3) * 3 + (i / 3)
            col = (boxIdx % 3) * 3 + (i % 3)
            yield (row, col)
    
    def hasDuplicate(self, board, positions):
        appeared = set()
        for row, col in positions:
            value = board[row][col]
            if value != '.' and value in appeared:
                return True
            appeared.add(value)
