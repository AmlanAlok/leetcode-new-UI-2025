# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return aug10_25(root)

def aug09_25(root):
    '''Recursive, TC = n, SC = n where n = total nodes in the tree'''
    
    def ismirror(x, y):

        if x is None and y is None:
            return True
        if x is None or y is None:
            return False
        
        return (
            (x.val == y.val) 
            and ismirror(x.right, y.left) 
            and ismirror(x.left, y.right)
        )
    
    return ismirror(root, root)

'''
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
[1,2,3]
[9,-42,-42,null,76,76,null,null,13,null,13]
'''
from collections import deque

def aug10_25(root):
    '''Iterative, TC = n, SC = n'''
    q = deque()
    q.append(root)
    q.append(root)

    while q:
        x = q.popleft()
        y = q.popleft()

        if x is None and y is None:
            continue
        if x is None or y is None:
            return False
        if x.val != y.val:
            return False
        
        q.append(x.left)
        q.append(y.right)
        q.append(x.right)
        q.append(y.left)
    
    return True
        