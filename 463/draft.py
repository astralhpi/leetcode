class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[i])):
                if self.isLand(grid, (i, j)):
                    for coordinate in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if not self.isLand(grid, coordinate):
                            result += 1
        return result
                    
    def isLand(self, grid, coordinate):
        i, j = coordinate
        if not (0 <= i < len(grid)):
            return False
        elif not (0 <= j < len(grid[i])):
            return False
        
        return grid[i][j] == 1
        
        
