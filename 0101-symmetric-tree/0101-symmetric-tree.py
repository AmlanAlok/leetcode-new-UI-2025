# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return aug09_25(root)

def aug09_25(root):
    '''Recursive, TC = n, SC = n where n = total nodes in the tree'''
    return ismirror(root, root)

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

'''
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
'''

    


        