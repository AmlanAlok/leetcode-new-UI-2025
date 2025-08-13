from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return aug12_25(root)

def aug12_25(root):
    '''TC = n, SC = n'''
    if root is None:
        return []

    return aug12_25(root.left) + aug12_25(root.right) + [root.val]



def ans_2(root):

    stack = deque()
    curr = root
    ans = []

    while stack or curr:

        if curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left

        else:
            curr = stack.pop()
            if len(stack) > 0 and curr.right == stack[-1]:
                temp = curr
                curr = stack.pop()
                stack.append(temp)
                # curr = curr.right
            else:
                ans.append(curr.val)
                curr = None

    return ans
                
        
def jan1(root):
    if root is None:
        return []
    
    return jan1(root.left) + jan1(root.right) + [root.val]

'''
[1,null,2,3]
[1,2,3,4,5,6,7]
'''
    
    
