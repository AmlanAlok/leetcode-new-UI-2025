# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return aug12_25(root)

def aug12_25(root):
    '''TC = n, SC = n'''
    
    if root is None:
        return []

    return [root.val] + aug12_25(root.left) + aug12_25(root.right)


    def ans_1(self, root):
        '''Recursive approach, TC = O(n), SC = O(n)'''
        if root is None:
            return []
        else:
            return [root.val] + self.ans_1(root.left) + self.ans_1(root.right)
    
    
    def ans_2(self, root):
        '''Stack Approach, TC = O(n), SC = O(n)'''

        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            root = stack.pop()
            
            if root:
                stack.append(root.right)
                stack.append(root.left)
                result.append(root.val)
                
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        