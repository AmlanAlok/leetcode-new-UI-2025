
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return sol(root, targetSum)
        return aug16_25(root, targetSum)


def aug16_25(root, t):

    if root is None:
        return False

    t = t - root.val

    if t == 0 and root.left is None and root.right is None:
        return True
    
    return aug16_25(root.left, t) or aug16_25(root.right, t)


    

'''
[5,4,8,11,null,13,4,7,2,null,null,null,1]
22
[1,2,3]
5
[]
0
'''

def jan3(root, t):
    
    if root is None:
        return False
    
    t -= root.val
    
    if root.left is None and root.right is None:
        return t == 0
    
    l = jan3(root.left, t)
    r = jan3(root.right, t)
    
    return l or r
    '''TC = N, SC = worst N or avg log(n)'''
    
def is_leaf(node):
	return node.left == None and node.right == None


def sol(root, targetSum):

	if root is None:
		return False

	targetSum -= root.val

	if targetSum == 0 and is_leaf(root):
		return True

	return sol(root.left, targetSum) or sol(root.right, targetSum)

