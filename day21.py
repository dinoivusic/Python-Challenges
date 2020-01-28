class Solution:
    def numIslands(self, grid):
        def changeLandToWater(grid, i, j):
            #row less than 0, row greater than grid length, column less than 0, column greater than grid[0] lenght, and if [i][j] is 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != "1":
                return 0

            grid[i][j] = ""

            changeLandToWater(grid, i - 1, j) #down
            changeLandToWater(grid, i + 1, j) # up
            changeLandToWater(grid, i, j - 1) # left
            changeLandToWater(grid, i, j + 1) # right
            return 1
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count += changeLandToWater(grid, i, j)
        return count
