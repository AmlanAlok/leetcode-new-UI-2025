# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return aug15_25(root, k)

def aug15_25(root, k):
    '''TC = n, SC = n'''
    s = set()

    def helper(root, k, s):
        
        if root is None:
            return False
        
        if k - root.val in s:
            return True
        
        s.add(root.val)

        return helper(root.left, k, s) or helper(root.right, k, s)

    return helper(root, k, s)

        