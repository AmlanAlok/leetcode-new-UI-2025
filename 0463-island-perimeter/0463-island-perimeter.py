class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return aug08_25(grid)

def aug07_25(grid):
    '''TC = m*n, SC = 1'''
    R = len(grid)
    C = len(grid[0])
    p = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                
                up = 0 if r == 0 else grid[r-1][c]
                down = 0 if r == R-1 else grid[r+1][c]
                left = 0 if c == 0 else grid[r][c-1]
                right = 0 if c == C-1 else grid[r][c+1]

                p += 4-up-down-left-right
    
    return p

def aug08_25(grid):
    '''TC = m*n, SC = 1'''
    R = len(grid)
    C = len(grid[0])
    p = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                
                p += 4

                if r > 0 and grid[r-1][c] == 1:
                    p -= 2

                if c > 0 and grid[r][c-1] == 1:
                    p -= 2
                
    return p

'''
[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
[[1]]
[[1,0]]
'''




def wrong01(grid):

    R = len(grid)
    C = len(grid[0])
    total = 0
    p = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                '''borders'''
                if r == 0 or r == R-1:
                    p += 1
                if c == 0 or c == C-1:
                    p += 1

                if 0 < c < C-1:
                    if grid[r][c+1] == 0:
                        p += 1
                    if grid[r][c-1] == 0:
                        p += 1
                
                if 0 < r < R-1:
                    if grid[r+1][c] == 0:
                        p += 1
                    if grid[r-1][c] == 0:
                        p += 1
    
    return p


    
