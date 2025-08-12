from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return aug12_25(root)

def aug12_25(root):

    if root is None:
        return []
    
    return aug12_25(root.left) + [root.val] + aug12_25(root.right)


    
def ans_1(root):

    if not root:
        return root

    e = []

    if root.left:
        e += self.ans_1(root.left)

    e.append(root.val)

    if root.right:
        e += self.ans_1(root.right)

    return e


def ans_2(root):
    ''' Recursion, TC = O(n), SC = O(n) '''
    '''
    TC = b*h = 2^(log2(n)) = n
    SC = Avg-log(n), worst=n
    '''
    if root is None:
        return []
    else:
        return self.ans_2(root.left) + [root.val] + self.ans_2(root.right)


def ans_3(root):    
    ''' Stack, TC = O(n), SC = O(n) '''
    if root is None:
        return []

    stack = deque()
    curr = root
    ans = []

    while stack or curr:

        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

    return ans
        
        
def jan2(root):
    
    if root is None:
        return []
    
    return jan2(root.left) + [root.val] + jan2(root.right)

def jan1(root):
    
    if root is None:
        return []
    
    stack = deque()
    cur = root
    ans = []
    
    
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
    
    return ans
            
    
    
        
