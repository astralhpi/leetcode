class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in xrange(0, 9):
            idxs_list = [self.row_indexes(i), self.col_indexes(i), self.box_indexes(i)]
            for idxs in idxs_list:
                if not self.is_valid_group(board, idxs):
                    return False
        return True
    
    def is_valid_group(self, board, indexes):
        used = set()
        for row, col in indexes:
            num = board[row][col]
            if num != '.' and num in used:
                return False
            elif num != '.':
                used.add(num)
        return True
    
    def row_indexes(self, row_idx):
        l = []
        for i in xrange(0, 9):
            l.append((row_idx, i))
        return l
    
    def col_indexes(self, col_idx):
        l = []
        for i in xrange(0, 9):
            l.append((i, col_idx))
        return l
    
    def box_indexes(self, box_idx):
        l = []
        for i in xrange(0, 9):
            row = int(box_idx / 3) * 3 + int(i/3)
            col = (box_idx % 3) * 3 + (i% 3)
            l.append((row, col))
        return l
            
        
if __name__ == "__main__":
    s = Solution()
    print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
