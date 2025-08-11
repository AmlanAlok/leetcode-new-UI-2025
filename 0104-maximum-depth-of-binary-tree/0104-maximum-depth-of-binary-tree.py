# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return aug10_25(root)


def aug10_25(root):
    '''Recursion, TC = n, SC = n in worst case and log(n) in best case'''
    
    if root is None:
        return 0
    
    l = aug10_25(root.left)
    r = aug10_25(root.right)

    return max(l, r) + 1



def max_depth(root: TreeNode):
    
    if root.left is None and root.right is None:
        return 1
    
    ans = None
    
    if root.left:
        v = max_depth(root.left) + 1
        if ans is None or ans < v:
            ans = v
    if root.right:
        v = max_depth(root.right) + 1
        if ans is None or ans < v:
            ans = v
    
    return ans
    
    
def ans1(root):
    if root:
        return max_depth(root)
    return 0
    
'''
TC = n
SC = 
worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N)

best case (the tree is completely balanced), the height of the tree would be log(N)
'''
def ans2(root):
    
    if root == None:
        return 0
    
    return 1 + max(ans2(root.left), ans2(root.right))
        
        
def p1(root):
    if root == None:
        return 0
    
    return 1 + max(p1(root.left), p1(root.right))


def jan3(root):
    
    if root is None:
        return 0
    
    l = jan3(root.left)
    r = jan3(root.right)
    
    return max(l, r) + 1



