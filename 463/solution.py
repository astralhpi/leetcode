class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[i])):
                result += self.countPermeter(grid, (i, j))
        return result
                  
    def countPermeter(self, grid, pos):
        if not self.isLand(grid, pos):
            return 0

        result = 0
        i, j = pos
        for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if not self.isLand(grid, neighbor):
                result += 1
        return result
        
    def isLand(self, grid, pos):
        i, j = pos
        if not (0 <= i < len(grid)):
            return False
        elif not (0 <= j < len(grid[i])):
            return False
        
        return grid[i][j] == 1
        
        
