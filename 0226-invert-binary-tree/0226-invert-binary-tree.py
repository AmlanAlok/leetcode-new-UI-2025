# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return aug10_25(root)

def aug10_25(root):
    '''TC = n, SC = n, where n = num of nodes in tree'''
    if root:
        root.left, root.right = aug10_25(root.right), aug10_25(root.left)

    return root

'''
[2,1,3]
[4,2,7,1,3,6,9]
[]
'''


    
def ans1(root):
    
    if root:
        
        # if root.left is None and root.right is None:
        #     return root
        

        l = ans1(root.left)
        r = ans1(root.right)
        root.right, root.left = l, r
         # if root.left:
        #     node = ans1(root.left)
        #     temp = root.left
        #     root.left = root.right
        #     root.right = temp
        # if root.right:
        #     node = ans1(root.right)
        #     temp = root.left
        #     root.left = root.right
        #     root.right = temp
    return root

def ans2(root):
    
    # if not root:
    if root is None:
        return None
    right = ans2(root.right)
    left = ans2(root.left)
    root.left = right
    root.right = left
    
    return root

def e1(root):
    
    if root.left is None and root.right is None:        # this lines fails in [] case
        return
    if root.left:
        p1(root.left)
    if root.right:
        p1(root.right)
    
    root.left, root.right = root.right, root.left
    
    return root

'''
Best answer yet
'''
def p1(root):
    
    if root:
        root.left, root.right = p1(root.right), p1(root.left)
    return root
    
