'''
11000
11000
00100
00011

'''
def numIslands(self, grid):
    if not grid:
        return 0
    counter = 0
    row = len(grid)
    col = len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c]=='1':
                self.dfs(grid, r,c)
                counter +=1
    return counter 
def dfs(self, grid, i, j):
    if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid,i+1,j)
    self.dfs(grid,i-1,j)
    self.dfs(grid,i,j+1)
    self.dfs(grid,i,j-1)
    