# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        return aug15_25(root, target)


def aug15_25(root, target):
    '''BST, TC = H, SC = 1 where H = height of the tree'''
    closest = root.val

    while root:
        n = root.val
        closest = min([n, closest], key = lambda x: (abs(x - target), x))   # important
        
        if target < n:
            root = root.left
        else:
            root = root.right
    
    return closest


def aug16_25(root, target):
    '''BST and Linear Search, TC = n, SC = n'''
    def inorder(node):

        if node is None:
            return []

        return inorder(node.left) + [node.val] + inorder(node.right)

    nums = inorder(root)

    return min(nums, key = lambda x: abs(x - target))


def aug16_25_fail(root, target):

    def helper(node, t):
        
        n = node.val

        if t < n:
            if node.left:
                l = node.left.val
                        
                if l < t < n:
                    return l if t - l <= 0.5 else n
                else:
                    return helper(node.left, t)
            else:
                return n
        elif n < t:
            if node.right:
                r = node.right.val

                if n < t < r:
                    return n if t - n <= 0.5 else r
                else:
                    return helper(node.right, t)
            else:
                return n
    
    if root:
        return helper(root, target)
    
    return None

    


        