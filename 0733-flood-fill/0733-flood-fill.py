class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # return aug08_25(image, sr, sc, color)
        return aug10_25(image, sr, sc, color)

def aug08_25(image, sr, sc, color):
    '''
    TC = n, where n = num of pixels in image
    SC = n, the recursion uses the runtime stack to put n stack frames
    '''

    R, C = len(image), len(image[0])
    cur = image[sr][sc]

    if cur == color:              # If current color is same as new color, it will lead to infinite recursion
        return image
    
    def dfs(r, c):
         if image[r][c] == cur:
            image[r][c] = color
            
            if r > 0:
                dfs(r-1, c)     # up
            if r + 1 < R:
                dfs(r+1, c)     # down
            if c > 0:
                dfs(r, c-1)     # left
            if c + 1 < C:
                dfs(r, c+1)     # right
    
    dfs(sr, sc)

    return image


'''
No Early Termination Check:
Originally, this check prevents unnecessary recursion if the newColor is the same as the starting pixel's color (color).
Without it, the code will proceed to DFS even if newColor == color, leading to redundant recursive calls.
Stack Overflow Risk (Infinite Recursion):
If newColor == color, the DFS will keep revisiting the same pixels and flipping them between color and newColor (which are the same).
This causes infinite recursion, eventually leading to a stack overflow (or a RecursionError in Python).
'''

def aug10_25(image, sr, sc, color):

    R, C = len(image), len(image[0])
    cur = image[sr][sc]

    if cur == color:
        return image

    def dfs(r, c):
        if image[r][c] == cur:
            image[r][c] = color

            if r > 0:
                dfs(r-1, c)
            if r+1 < R:
                dfs(r+1, c)
            if c > 0:
                dfs(r, c-1)
            if c+1 < C:
                dfs(r, c+1)
            
    dfs(sr, sc)

    return image
    
